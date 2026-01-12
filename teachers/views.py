from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import StaffProfile
from .forms import StaffProfileForm


@login_required
def list_staff(request):
    staff_list = StaffProfile.objects.all().order_by("full_name")

    # Attach a bound edit form to each staff object (for modal editing)
    for staff in staff_list:
        staff.form = StaffProfileForm(instance=staff)

    context = {
        "staff_list": staff_list,
        "form": StaffProfileForm(),  # create form
    }

    return render(request, "teachers/staff_list.html", context)

@login_required
def create_staff(request):
    if request.method != "POST":
        return redirect("teachers:list_staff")

    form = StaffProfileForm(request.POST)

    if form.is_valid():
        staff = form.save(commit=False)
        staff.added_by = request.user
        staff.save()

        messages.success(request, "Staff profile created successfully.")
    else:
        messages.error(request, "Please correct the errors and try again.")

    return redirect("teachers:list_staff")


@login_required
def edit_staff(request, staff_id):
    staff = get_object_or_404(StaffProfile, id=staff_id)

    if request.method != "POST":
        return redirect("teachers:list_staff")

    form = StaffProfileForm(request.POST, instance=staff)

    if form.is_valid():
        form.save()
        messages.success(request, "Staff profile updated successfully.")
    else:
        messages.error(request, "Please correct the errors and try again.")

    return redirect("teachers:list_staff")


@login_required
def delete_staff(request, staff_id):
    staff = get_object_or_404(StaffProfile, id=staff_id)
    staff.delete()

    messages.success(request, "Staff profile deleted successfully.")
    return redirect("teachers:list_staff")
