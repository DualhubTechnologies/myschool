from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied, FieldError
from django.db import transaction

from teachers.models import StaffProfile, TeacherSubject
from schoolprofile.models import Subject
from accounts.models import Role, UserRole
from django.conf import settings
from django.core.mail import send_mail

User = get_user_model()


from django.shortcuts import render, redirect
from django.core.exceptions import FieldError, PermissionDenied
from django.db import transaction

def staff_accounts_page(request):
    current_user = request.user

    # ---------------------------
    # DATA FOR PAGE
    # ---------------------------

    try:
        roles = Role.objects.filter(user=current_user).order_by("name")
    except FieldError:
        roles = Role.objects.all().order_by("name")

    staff_list = (
        StaffProfile.objects
        .select_related("user")
        .order_by("full_name")
    )

    subjects = list(Subject.objects.all())

    staff_ids = list(staff_list.values_list("id", flat=True))
    staff_subjects = {sid: [] for sid in staff_ids}

    for staff_id, subject_id in (
        TeacherSubject.objects
        .filter(staff_id__in=staff_ids)
        .values_list("staff_id", "subject_id")
    ):
        staff_subjects.setdefault(staff_id, []).append(subject_id)

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
    # HANDLE POST
    # ---------------------------
    if request.method == "POST":
        action = request.POST.get("action", "save")
        staff_id = request.POST.get("staff_id")

        if not staff_id:
            return redirect("accounts:staff_accounts_page")

        staff = StaffProfile.objects.select_related("user").get(id=staff_id)

        # ---------------------------
        # DELETE USER ACCOUNT
        # ---------------------------
        if action == "delete":
            if not staff.user:
                return redirect("accounts:staff_accounts_page")

            if staff.user == request.user:
                raise PermissionDenied("You cannot delete your own account.")

            with transaction.atomic():
                user = staff.user

                UserRole.objects.filter(user=user).delete()
                TeacherSubject.objects.filter(staff=staff).delete()

                staff.user = None
                staff.save(update_fields=["user"])

                user.delete()

            return redirect("accounts:staff_accounts_page")

        # ---------------------------
        # CREATE / UPDATE USER
        # ---------------------------
        role_id = request.POST.get("role")
        subject_ids = request.POST.getlist("subjects")
        email = (request.POST.get("email") or "").strip()
        password = (request.POST.get("password") or "").strip()
        is_active = request.POST.get("is_active") == "on"

        if not role_id:
            return redirect("accounts:staff_accounts_page")

        role = Role.objects.get(id=role_id)

        with transaction.atomic():
            # UPDATE
            if staff.user:
                target_user = staff.user
                target_user.is_active = is_active

                if email:
                    target_user.email = email

                if password:
                    target_user.set_password(password)

                update_fields = ["is_active"]
                if email:
                    update_fields.append("email")
                if password:
                    update_fields.append("password")

                target_user.save(update_fields=update_fields)

            # CREATE
            else:
                if not password:
                    raise ValueError("Password is required when creating a user.")

                extra_fields = {
                    "is_staff": True,
                    "is_active": is_active,
                }

                user_field_names = {f.name for f in User._meta.get_fields()}
                if "user" in user_field_names:
                    extra_fields["user"] = current_user

                target_user = User.objects.create_user(
                    email=email,
                    password=password,
                    **extra_fields,
                )

                staff.user = target_user
                staff.save(update_fields=["user"])

                # 5. Send email with account details
                

                subject = "Your Schoolsys Account Has Been Created"

                message = (
                    "Hello,\n\n"
                    "Your Schoolsys account has been successfully created.\n\n"
                    "Please use the link below to log in to the system:\n\n"
                    f"👉 Press here to login: {settings.CUSTOM_LOGIN_URL}\n\n"
                    "Login details:\n"
                    f"Email: {email}\n"
                    f"Temporary Password: {password}\n\n"
                    "You will be required to change your password upon your first login.\n\n"
                    "Regards,\n"
                    "The Schoolsys Team"
                )

                send_mail(
                    subject,
                    message,
                    None,              # Uses DEFAULT_FROM_EMAIL
                    [email],
                    fail_silently=False,
                )

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
            # ASSIGN SUBJECTS (TEACHERS)
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
            "staff_subjects": staff_subjects,
            "user_roles": user_roles,
        },
    )
