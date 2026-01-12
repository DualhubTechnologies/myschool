from django.db import models
from django.forms import ValidationError

class SchoolProfile(models.Model):
    motto = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to="school/logo/", null=True, blank=True)
    banner = models.ImageField(upload_to="school/banner/", null=True, blank=True)

    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)

    address = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)

    school_type = models.CharField(
        max_length=50,
        choices=[
            ("nursery", "Nursery"),
            ("primary", "Primary"),
            ("secondary", "Secondary"),

        ],
        default="primary",
    )

    ownership = models.CharField(
        max_length=20,
        choices=[("private", "Private"), ("government", "Government"), ("ngo", "NGO")],
        default="private",
    )

    registration_number = models.CharField(max_length=100, blank=True)

    academic_year_start = models.DateField(null=True, blank=True)
    academic_year_end = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.motto


class Level(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('name',)

    def __str__(self):
        return self.name


class SchoolClass(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('level', 'name')

    def __str__(self):
        return f"{self.name} ({self.level})"

    @property
    def assigned_subjects(self):
        # Returns ClassSubject queryset
        from schoolprofile.models import ClassSubject
        return ClassSubject.objects.filter(school_class=self)



class Stream(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('school_class', 'name')

    def __str__(self):
        return f"{self.school_class} - {self.name}"
    


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    short_name = models.CharField(max_length=50, blank=True)

    # Generic — school decides classification
    number_of_papers = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        ordering = ["name"]


class ClassSubject(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    # Classification for that specific class
    is_mandatory = models.BooleanField(default=True)
    is_optional = models.BooleanField(default=False)

    # Optional subject limits (if needed)
    min_students = models.PositiveIntegerField(default=0)
    max_students = models.PositiveIntegerField(default=60)

    def clean(self):
        if self.is_mandatory and self.is_optional:
            raise ValidationError("A subject cannot be both mandatory and optional.")

        if not self.is_mandatory and not self.is_optional:
            raise ValidationError("A subject must be either mandatory or optional.")

    class Meta:
        unique_together = ("school_class", "subject")

    def __str__(self):
        type_label = "Mandatory" if self.is_mandatory else "Optional"
        return f"{self.school_class} → {self.subject.name} ({type_label})"
