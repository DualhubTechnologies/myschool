from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Subject, ClassSubject,  SchoolClass
from schoolprofile.forms import SubjectForm


@login_required
def list_subjects(request):
    subjects = Subject.objects.all().order_by("name")

    # Add an attached form instance for each subject (used in modals)
    for s in subjects:
        s.form = SubjectForm(instance=s, request=request)

    return render(request, "schoolprofile/subjects_list.html", {
        "subjects": subjects,
        "form": SubjectForm(request=request),   # for Add modal
    })


@login_required
def add_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST, request=request)

        if form.is_valid():
            subject = form.save(commit=False)

            subject.save()
            messages.success(request, "Subject created successfully.")
        else:
            messages.error(request, "Could not save subject. Check form fields.")

    return redirect("profile:list_subjects")


@login_required
def edit_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)

    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject, request=request)

        if form.is_valid():
            updated = form.save(commit=False)

            updated.save()
            messages.success(request, "Subject updated successfully.")
        else:
            messages.error(request, "Could not update subject.")

    return redirect("profile:list_subjects")


@login_required
def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    name = subject.name
    subject.delete()

    messages.success(request, f"Subject '{name}' deleted successfully.")
    return redirect("profile:list_subjects")

@login_required
def assign_subjects_to_class(request, class_id):
    school_class = get_object_or_404(SchoolClass, id=class_id)

    if request.method == "POST":
        selected_ids = request.POST.getlist("subject_ids")

        # Remove unselected
        ClassSubject.objects.filter(
            school_class=school_class
        ).exclude(subject_id__in=selected_ids).delete()

        # Add/update selected
        for subject_id in selected_ids:
            type_value = request.POST.get(f"type_{subject_id}")
            is_mandatory = (type_value == "mandatory")

            ClassSubject.objects.update_or_create(
                school_class=school_class,
                subject_id=subject_id,
                defaults={
                    "is_mandatory": is_mandatory,
                    "is_optional": not is_mandatory
                }
            )

        messages.success(request, "Subjects assigned successfully.")
        return redirect("profile:list_classes")