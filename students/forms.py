from django import forms

from schoolprofile.models import Stream
from students.models import Student

from django import forms
from schoolprofile.models import Stream
from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'admission_number',
            'Lin',
            'schoolpay_code',
            'first_name',
            'last_name',
            'other_names',
            'status',
            'level',
            'school_class',
            'stream',
            'student_type',
            'gender',
            'date_of_birth',
            'parent_name',
            'parent_contact',
            'address',
            'photo',
            'uce_index_number',
            'uace_index_number',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')

        self.fields['stream'].queryset = Stream.objects.none()

        if 'school_class' in self.data:
            try:
                school_class_id = int(self.data.get('school_class'))
                self.fields['stream'].queryset = Stream.objects.filter(
                    school_class_id=school_class_id
                )
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.school_class:
            self.fields['stream'].queryset = Stream.objects.filter(
                school_class=self.instance.school_class
            )

        
class UploadExcelForm(forms.Form):
    excel_file = forms.FileField(
        label="Excel or CSV file",
        help_text="Upload .xlsx, .xls or .csv",
        widget=forms.ClearableFileInput(attrs={'accept':'.xlsx,.xls,.csv'})
    )