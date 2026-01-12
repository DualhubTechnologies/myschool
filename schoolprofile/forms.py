from django import forms
from .models import Level, SchoolClass, SchoolProfile, Stream, Subject

class SchoolProfileForm(forms.ModelForm):

    class Meta:
        model = SchoolProfile
        fields = [
            "motto",
            "logo",
            "banner",
            "contact_email",
            "contact_phone",
            "website",
            "address",
            "district",
            "region",
            "school_type",
            "ownership",
            "registration_number",
            "academic_year_start",
            "academic_year_end",
        ]

        widgets = {
            "motto": forms.TextInput(attrs={"class": "form-control"}),
            "contact_email": forms.EmailInput(attrs={"class": "form-control"}),
            "contact_phone": forms.TextInput(attrs={"class": "form-control"}),
            "website": forms.URLInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "district": forms.TextInput(attrs={"class": "form-control"}),
            "region": forms.TextInput(attrs={"class": "form-control"}),
            "registration_number": forms.TextInput(attrs={"class": "form-control"}),
            "academic_year_start": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "academic_year_end": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "school_type": forms.Select(attrs={"class": "form-select"}),
            "ownership": forms.Select(attrs={"class": "form-select"}),
        }

class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

class SchoolClassForm(forms.ModelForm):
    class Meta:
        model = SchoolClass
        fields = ["level", "name"]

        widgets = {
            "level": forms.Select(attrs={"class": "form-select"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = ["school_class", "name"]

        widgets = {
            "school_class": forms.Select(attrs={"class": "form-select"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
        
class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = [
            "name",
            "code",
            "short_name",
            "number_of_papers",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "code": forms.TextInput(attrs={"class": "form-control"}),
            "short_name": forms.TextInput(attrs={"class": "form-control"}),
            "number_of_papers": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 1
            }),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

        # Nursery/Primary subjects ALWAYS have 1 paper — hide the field
        school_type = getattr(self.request, "school_type", "primary")

        if school_type in ["nursery", "primary"]:
            self.fields["number_of_papers"].widget = forms.HiddenInput()
            self.fields["number_of_papers"].initial = 1


