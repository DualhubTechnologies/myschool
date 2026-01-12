from django.db import models
from django.conf import settings
from django.forms import ValidationError
from schoolprofile.models import Subject

EMPLOYMENT_TYPE_CHOICES = [
    ("full_time", "Full Time"),
    ("part_time", "Part Time"),
    ("contract", "Contract"),
    ("volunteer", "Volunteer"),
    ("temporary", "Temporary"),
]
highest_qualification_choices = [
    ("bachelor", "Bachelor's Degree"),
    ("master", "Master's Degree"),
    ("doctorate", "Doctorate"),
    ("diploma", "Diploma"),
    ("certificate", "Certificate"),
]

class StaffProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="+", )

    full_name = models.CharField(max_length=255, default="")
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)

    phone = models.CharField(max_length=32, blank=True)
    contact_person = models.CharField(max_length=255, blank=True)

    employee_id = models.CharField(max_length=50, unique=True)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)

    highest_qualification = models.CharField(
        max_length=20,
        choices=highest_qualification_choices,
        null=True, blank=True,
    )
    professional_certifications = models.TextField(blank=True)

    date_of_employment = models.DateField(null=True, blank=True)
    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default="full_time"
    )

    # Audit
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.DO_NOTHING,
        related_name="+",
        
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.job_title}"



class TeacherSubject(models.Model):
    staff = models.ForeignKey(
        StaffProfile,
        on_delete=models.CASCADE,
        related_name="subjects"
    )
    subject = models.ForeignKey(
        "schoolprofile.Subject",
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("staff", "subject")

    def clean(self):
        if self.staff.role != "teacher":
            raise ValidationError("Only staff with role 'Teacher' can be assigned subjects.")
