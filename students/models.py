from django.db import models
from schoolprofile.models import SchoolClass, Stream
from schoolprofile.models import Subject   # Still needed elsewhere
from schoolprofile.models import ClassSubject

 
class Student(models.Model):

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    STUDENT_TYPE_CHOICES = [
        ("DAY", "Day Scholar"),
        ("BOARDING", "Boarding"),
    ]

    LEVEL_CHOICES = [
        ("NURSERY", "Nursery"),
        ("PRIMARY", "Primary"),
        ("OLEVEL", "O-Level"),
        ("ALEVEL", "A-Level"),
    ]
    STATUS_CHOICES = [
        ('active',    'Active'),
        ('suspended', 'Suspended'),
        ('expelled',  'Expelled'),
        ('deceased',  'Deceased'),
        ('unknown',   'Unknown'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    other_names = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
        help_text="Current enrollment status",
        blank=True, null=True
    )

    photo = models.ImageField(
        upload_to='student_photos/',
        blank=True,
        null=True,
        default='student_photos/default.png',
        help_text="Upload a student photo"
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)

    admission_number = models.CharField(max_length=50, unique=True)
    admission_date = models.DateField(auto_now_add=True)
    schoolpay_code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    Lin = models.CharField(max_length=50, unique=True, blank=True, null=True)
    

    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, null=True, blank=True)

    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students"
    )

    stream = models.ForeignKey(
        Stream,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students"
    )

    student_type = models.CharField(
        max_length=10,
        choices=STUDENT_TYPE_CHOICES,
        default="DAY",
        blank=True, null=True
    )

    # Uganda exam references
    uce_index_number = models.CharField(max_length=50, blank=True)
    uace_index_number = models.CharField(max_length=50, blank=True)

    parent_name = models.CharField(max_length=255, blank=True)
    parent_contact = models.CharField(max_length=50, blank=True)

    address = models.CharField(max_length=255, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.admission_number} - {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.other_names} {self.last_name}".strip()

class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class_subject = models.ForeignKey(
        Subject,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="student_subjects"
    )

    # This is derived from ClassSubject but stored for convenience
    is_optional = models.BooleanField(default=False)

    class Meta:
        unique_together = ("student", "class_subject")

    def __str__(self):
        return f"{self.student.full_name} → {self.class_subject.subject.name}"