from django import forms
from django.contrib.auth.forms import AuthenticationForm

class StyledAuthForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
    )


# accounts/forms.py

from django import forms
from accounts.models import Role
from schoolprofile.models import Subject


class StaffAccountCreateForm(forms.Form):
    staff_id = forms.CharField(
        label="Staff ID",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    full_name = forms.CharField(
        label="Full Name",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "readonly": True
        })
    )

    role = forms.ModelChoiceField(
        queryset=Role.objects.none(),
        widget=forms.Select(attrs={"class": "form-control"})
    )

    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.none(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user:
            self.fields["role"].queryset = Role.objects.filter(user=user)

        # Subjects loaded dynamically in view (user schema)
