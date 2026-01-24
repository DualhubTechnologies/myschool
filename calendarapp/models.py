from django.db import models
from django.core.exceptions import ValidationError

class AcademicYear(models.Model):
    year = models.CharField(max_length=9, unique=True)  
    # e.g. "2024", or "2024/2025"

    start_date = models.DateField()
    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date.")

    def __str__(self):
        return self.year


class SchoolTerm(models.Model):

    TERM_CHOICES = [
        ("term1", "Term 1"),
        ("term2", "Term 2"),
        ("term3", "Term 3"),
    ]

    academic_year = models.ForeignKey(AcademicYear,
                                      on_delete=models.CASCADE,
                                      related_name="terms")

    name = models.CharField(max_length=10, choices=TERM_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("academic_year", "name")
        ordering = ["start_date"]

    def clean(self):
        # Term must stay inside its academic year
        if self.start_date < self.academic_year.start_date or \
           self.end_date > self.academic_year.end_date:
            raise ValidationError("Term dates must be inside the academic year's date range.")

        # No overlapping within the same year
        qs = SchoolTerm.objects.filter(academic_year=self.academic_year).exclude(id=self.id)
        for term in qs:
            if self.start_date <= term.end_date and self.end_date >= term.start_date:
                raise ValidationError(
                    f"{self.get_name_display()} overlaps with {term.get_name_display()}."
                )

        if self.end_date < self.start_date:
            raise ValidationError("Term end date cannot be before start date.")

    def __str__(self):
        return f"{self.get_name_display()} - {self.academic_year.year}"


class SchoolEvent(models.Model):
    title = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50, choices=[
        ("primary", "Primary"),
        ("success", "Success"),
        ("warning", "Warning"),
        ("danger", "Danger"),
        ("info", "Info"),
    ])
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    url = models.URLField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title