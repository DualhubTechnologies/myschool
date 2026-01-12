# teachers/views_staff_accounts.py

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied, FieldError
from django.db import transaction

from teachers.models import StaffProfile, TeacherSubject
from schoolprofile.models import Subject
from accounts.models import Role, UserRole

User = get_user_model()


def staff_accounts_page(request):
    # Permission gate
    if not request.user.has_permission("staff.manage"):
        raise PermissionDenied

    current_user = request.user

    # ---------------------------
    # DATA FOR PAGE (single schema)
    # ---------------------------

    # Roles for dropdown (keep your original filter if Role has a FK to user; otherwise fallback to all roles)
    try:
        roles = Role.objects.filter(user=current_user).order_by("name")
    except FieldError:
        roles = Role.objects.all().order_by("name")

    # Staff list
    staff_list = (
        StaffProfile.objects
        .select_related("user")
        .order_by("full_name")
    )

    # Subjects
    subjects = list(Subject.objects.all())

    # Build staff -> [subject_id, ...] map efficiently
    staff_ids = list(staff_list.values_list("id", flat=True))
    staff_subjects = {sid: [] for sid in staff_ids}

    for staff_id, subject_id in (
        TeacherSubject.objects
        .filter(staff_id__in=staff_ids)
        .values_list("staff_id", "subject_id")
    ):
        staff_subjects.setdefault(staff_id, []).append(subject_id)

    # Build user_id -> Role map for users linked to staff
    staff_user_ids = [u for u in staff_list.values_list("user_id", flat=True) if u]
    user_roles = {
        ur.user_id: ur.role
        for ur in (
            UserRole.objects
            .filter(user_id__in=staff_user_ids)
            .select_related("role")
        )
    }

    # ---------------------------
    # HANDLE POST (create/update staff user + assign role + subjects)
    # ---------------------------
    if request.method == "POST":
        staff_id = request.POST.get("staff_id")
        role_id = request.POST.get("role")
        subject_ids = request.POST.getlist("subjects")
        email = (request.POST.get("email") or "").strip()
        password = request.POST.get("password") or ""
        is_active = request.POST.get("is_active") == "on"

        # Basic safety
        if not staff_id or not role_id:
            return redirect("accounts:staff_accounts_page")

        role = Role.objects.get(id=role_id)
        staff = StaffProfile.objects.select_related("user").get(id=staff_id)

        with transaction.atomic():
            # ---------------------------
            # CREATE / UPDATE USER
            # ---------------------------
            if staff.user:
                target_user = staff.user
                target_user.is_active = is_active

                # Optionally update email if provided
                if email:
                    setattr(target_user, "email", email)

                # Optionally update password if provided
                if password:
                    target_user.set_password(password)

                # Save only what changed
                update_fields = ["is_active"]
                if email:
                    update_fields.append("email")
                if password:
                    # set_password touches password hash; include "password"
                    update_fields.append("password")

                target_user.save(update_fields=update_fields)

            else:
                # Build extra fields safely (only pass fields that exist on your User model)
                extra_fields = {"is_staff": True, "is_active": is_active}

                user_field_names = {f.name for f in User._meta.get_fields()}
                if "user" in user_field_names:
                    # If your custom User model has a FK like user=<creator/admin>
                    extra_fields["user"] = current_user

                # Create the user
                target_user = User.objects.create_user(
                    email=email,
                    password=password,
                    **extra_fields,
                )

                # Link staff to this user
                staff.user = target_user
                staff.save(update_fields=["user"])

            # ---------------------------
            # ASSIGN ROLE
            # ---------------------------
            UserRole.objects.filter(user=target_user).delete()
            UserRole.objects.create(
                user=target_user,
                role=role,
                assigned_by=current_user,
            )

            # ---------------------------
            # ASSIGN SUBJECTS (teachers only)
            # ---------------------------
            TeacherSubject.objects.filter(staff=staff).delete()

            if (role.name or "").lower() == "teacher":
                TeacherSubject.objects.bulk_create([
                    TeacherSubject(staff=staff, subject_id=sid)
                    for sid in subject_ids
                ])

        return redirect("accounts:staff_accounts_page")

    # ---------------------------
    # RENDER
    # ---------------------------
    return render(
        request,
        "teachers/staff_accounts.html",
        {
            "staff_list": staff_list,
            "roles": roles,
            "subjects": subjects,
            "staff_subjects": staff_subjects,  # staff_id -> [subject_id, ...]
            "user_roles": user_roles,          # user_id -> Role
        },
    )
