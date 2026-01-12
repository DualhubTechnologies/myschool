from django import forms
from .models import SchoolProfile
from django.contrib.auth.decorators import login_required

from .models import Level, SchoolClass, Stream
from schoolprofile.forms import LevelForm, SchoolClassForm, StreamForm


from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import SchoolProfile
from schoolprofile.models import Subject
from .forms import SchoolProfileForm


def school_profile(request):
    user = request.user
    profile, created = SchoolProfile.objects.get_or_create(id=1)

    return render(request, "schoolprofile/profile_view.html", {
        "profile": profile,
        "user": user,
    })



def edit_school_profile(request):
    profile, created = SchoolProfile.objects.get_or_create(id=1)
    user = request.user

    if request.method == "POST":
        form = SchoolProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "School profile updated successfully.")
            return redirect("profile:school_profile")
    else:
        form = SchoolProfileForm(instance=profile)

    return render(request, "schoolprofile/profile_edit.html", {
        "form": form,
        "user": user,
        "profile": profile
    })


# =============================
#          LEVELS
# =============================

@login_required
def list_levels(request):
    levels = Level.objects.all()

    if request.method == "POST":
        form = LevelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Level added successfully.")
            return redirect("profile:list_levels")
    else:
        form = LevelForm()

    # Provide edit forms for modal editing
    for lvl in levels:
        lvl.form = LevelForm(instance=lvl)

    return render(request, "schoolprofile/levels.html", {
        "levels": levels,
        "form": form,
    })


@login_required
def edit_level(request, level_id):
    level = get_object_or_404(Level, id=level_id)

    if request.method == "POST":
        form = LevelForm(request.POST, instance=level)
        if form.is_valid():
            form.save()
            messages.success(request, "Level updated successfully.")
            return redirect("profile:list_levels")
        else:
            messages.error(request, "Please correct the errors.")
            return redirect("profile:list_levels")

    return redirect("profile:list_levels")


@login_required
def delete_level(request, level_id):
    level = get_object_or_404(Level, id=level_id)
    level.delete()
    messages.success(request, "Level deleted successfully.")
    return redirect("profile:list_levels")


# =============================
#           CLASSES
# =============================

@login_required
def list_classes(request):
    classes = SchoolClass.objects.select_related("level").all()
    subjects = Subject.objects.all()   # For Assign Subjects popup

    # Handle Add Class POST
    if request.method == "POST":
        form = SchoolClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Class added successfully.")
            return redirect("profile:list_classes")
    else:
        form = SchoolClassForm()

    # Attach edit form per row
    for c in classes:
        c.form = SchoolClassForm(instance=c)

    return render(request, "schoolprofile/classes.html", {
        "classes": classes,
        "subjects": subjects,      # <-- needed for the popup
        "form": form,
    })


@login_required
def edit_class(request, class_id):
    school_class = get_object_or_404(SchoolClass, id=class_id)

    if request.method == "POST":
        form = SchoolClassForm(request.POST, instance=school_class)
        if form.is_valid():
            form.save()
            messages.success(request, "Class updated successfully.")
            return redirect("profile:list_classes")
        else:
            messages.error(request, "Please correct the errors.")
            return redirect("profile:list_classes")

    return redirect("profile:list_classes")


@login_required
def delete_class(request, class_id):
    school_class = get_object_or_404(SchoolClass, id=class_id)
    school_class.delete()
    messages.success(request, "Class deleted successfully.")
    return redirect("profile:list_classes")


# =============================
#          STREAMS
# =============================

@login_required
def list_streams(request):
    streams = Stream.objects.select_related("school_class", "school_class__level")

    if request.method == "POST":
        form = StreamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Stream added successfully.")
            return redirect("profile:list_streams")
    else:
        form = StreamForm()

    # prepare edit forms
    for s in streams:
        s.form = StreamForm(instance=s)

    return render(request, "schoolprofile/streams.html", {
        "streams": streams,
        "form": form,
    })


@login_required
def edit_stream(request, stream_id):
    stream = get_object_or_404(Stream, id=stream_id)

    if request.method == "POST":
        form = StreamForm(request.POST, instance=stream)
        if form.is_valid():
            form.save()
            messages.success(request, "Stream updated successfully.")
            return redirect("profile:list_streams")
        else:
            messages.error(request, "Fix the errors and try again.")
            return redirect("profile:list_streams")

    return redirect("profile:list_streams")


@login_required
def delete_stream(request, stream_id):
    stream = get_object_or_404(Stream, id=stream_id)
    stream.delete()
    messages.success(request, "Stream deleted successfully.")
    return redirect("profile:list_streams")
