from django import forms
from .models import AcademicYear, SchoolTerm, SchoolEvent

class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = ["year", "start_date", "end_date"]
        widgets = {
            "year": forms.TextInput(attrs={"class": "form-control", "placeholder": "2025"}),
            "start_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "end_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }


class SchoolTermForm(forms.ModelForm):
    class Meta:
        model = SchoolTerm
        fields = ["academic_year", "name", "start_date", "end_date"]

        widgets = {
            "academic_year": forms.Select(attrs={"class": "form-select"}),
            "name": forms.Select(attrs={"class": "form-select"}),
            "start_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "end_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }



class SchoolEventForm(forms.ModelForm):
    class Meta:
        model = SchoolEvent
        fields = ["title", "event_type", "start", "end", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "event_type": forms.Select(attrs={"class": "form-select"}),
            "start": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "end": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
