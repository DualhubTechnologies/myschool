from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import json

from .models import SchoolEvent, AcademicYear, SchoolTerm
from .forms import AcademicYearForm, SchoolTermForm


def calendar_page(request):
    """Render the calendar UI"""
    return render(request, "calendarapp/calendar.html")


def get_events(request):
    """Return events as JSON for FullCalendar"""
    events = SchoolEvent.objects.all()

    data = [
        {
            "id": e.id,
            "title": e.title,
            "start": e.start.isoformat(),
            "end": e.end.isoformat() if e.end else None,
            "className": f"bg-{e.event_type}",
            "description": e.description,
            "location": e.location,
            "url": e.url or "",
        }
        for e in events
    ]

    return JsonResponse(data, safe=False)


@csrf_exempt
def add_event(request):
    """Add event through AJAX POST"""
    if request.method == "POST":
        data = json.loads(request.body)

        SchoolEvent.objects.create(
            title=data["title"],
            event_type=data["label"],
            start=data["start"],
            end=data.get("end"),
            url=data.get("url", ""),
            location=data.get("location", ""),
            description=data.get("description", "")
        )

        return JsonResponse({"success": True})

    return JsonResponse({"error": "Invalid request"}, status=400)


# ------------------------------
#         Academic Years
# ------------------------------

@login_required
def list_academic_years(request):
    years = AcademicYear.objects.all()

    if request.method == "POST":
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Academic Year added successfully.")
            return redirect("calendar:list_academic_years")
    else:
        form = AcademicYearForm()

    return render(request, "calendarapp/academic_year.html", {
        "years": years,
        "form": form,
    })


@login_required
def add_academic_year(request):
    if request.method == "POST":
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Academic year created.")
            return redirect("calendar:list_academic_years")
    else:
        form = AcademicYearForm()

    return render(request, "calendarapp/academic_year.html", {"form": form})


# ------------------------------
#             Terms
# ------------------------------

@login_required
def list_terms(request):
    terms = SchoolTerm.objects.select_related("academic_year")

    if request.method == "POST":
        form = SchoolTermForm(request.POST)

        if form.is_valid():
            academic_year = form.cleaned_data["academic_year"]
            start = form.cleaned_data["start_date"]
            end = form.cleaned_data["end_date"]

            overlapping = SchoolTerm.objects.filter(
                academic_year=academic_year,
                start_date__lte=end,
                end_date__gte=start
            )

            if overlapping.exists():
                messages.error(request, "This term overlaps with an existing term.")
                return redirect("calendar:list_terms")

            form.save()
            messages.success(request, "Term created successfully.")
            return redirect("calendar:list_terms")

    else:
        form = SchoolTermForm()

    # Add edit form to each term for modal use
    for t in terms:
        t.form = SchoolTermForm(instance=t)

    return render(request, "calendarapp/school_terms.html", {
        "terms": terms,
        "form": form,
    })



@login_required
def add_term(request):
    if request.method == "POST":
        form = SchoolTermForm(request.POST)
        if form.is_valid():

            # ✔ Prevent Overlapping Terms
            academic_year = form.cleaned_data["academic_year"]
            start = form.cleaned_data["start_date"]
            end = form.cleaned_data["end_date"]

            overlapping = SchoolTerm.objects.filter(
                academic_year=academic_year,
                start_date__lte=end,
                end_date__gte=start
            )

            if overlapping.exists():
                messages.error(request, "Term dates overlap with an existing term.")
                return redirect("calendar:add_term")

            form.save()
            messages.success(request, "Term created successfully.")
            return redirect("calendar:list_terms")

    else:
        form = SchoolTermForm()

    return render(request, "calendarapp/school_terms.html", {"form": form})

@login_required
def edit_term(request, term_id):
    term = SchoolTerm.objects.get(id=term_id)

    if request.method == "POST":
        form = SchoolTermForm(request.POST, instance=term)

        if form.is_valid():
            # Prevent overlapping terms (excluding itself)
            academic_year = form.cleaned_data["academic_year"]
            start = form.cleaned_data["start_date"]
            end = form.cleaned_data["end_date"]

            overlapping = SchoolTerm.objects.filter(
                academic_year=academic_year,
                start_date__lte=end,
                end_date__gte=start
            ).exclude(id=term.id)

            if overlapping.exists():
                messages.error(request, "This term overlaps with another existing term.")
                return redirect("calendar:list_terms")

            form.save()
            messages.success(request, "Term updated successfully.")
            return redirect("calendar:list_terms")

        else:
            # form invalid
            messages.error(request, "Please correct the errors in the form.")
            return redirect("calendar:list_terms")

    # If accessed via GET, just redirect
    return redirect("calendar:list_terms")

@login_required
def delete_term(request, term_id):
    term = SchoolTerm.objects.get(id=term_id)
    term.delete()
    messages.success(request, "Term deleted successfully.")
    return redirect("calendar:list_terms")