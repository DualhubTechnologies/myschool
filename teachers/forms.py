from django import forms
from .models import StaffProfile


class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile

        # Exclude system / audit fields
        exclude = (
            "user",
            "added_by",
            "created_at",
            "updated_at",
            "job_title",
        )

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "employee_id": forms.TextInput(attrs={"class": "form-control"}),
            "department": forms.TextInput(attrs={"class": "form-control"}),
            "nationality": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "contact_person": forms.TextInput(attrs={"class": "form-control"}),

            "date_of_birth": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "date_of_employment": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),

            "highest_qualification": forms.Select(attrs={"class": "form-select"}),
            "employment_type": forms.Select(attrs={"class": "form-select"}),

            "professional_certifications": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),

            "user": forms.Select(attrs={"class": "form-select"}),
        }
