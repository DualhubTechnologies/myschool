from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from students.forms import StudentForm,  UploadExcelForm
from django.db.models import Count, Q
from schoolprofile.models import SchoolClass, Stream
from students.models import  Student
from django.contrib import messages
from .excel import import_students_from_excel
from django.views.decorators.http import require_POST
from django_currentuser.middleware import _set_current_user

app_name = "students"


def addstudent(request):
    _set_current_user(request.user)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:studentDetails') 
        else:
            print("FORM ERRORS:", form.errors) 
    else:
        form = StudentForm()
    return render(request, 'students/addstudent.html', {'form': form})

def studentDetails(request):
        students = Student.objects.select_related('school_class', 'stream').all()
        return render(request, 'students/studentlist.html', {'students': students})


def studentDetails(request):
    # Start with a base queryset
    students = Student.objects.select_related('school_class', 'stream')

    # Get filter values from GET parameters
    filters = {
        'school_class': request.GET.get('school_class', ''),
        'stream': request.GET.get('stream', ''),
        'section': request.GET.get('section', ''),
        'status': request.GET.get('status', '')
    }

    # Apply filters based on provided criteria, but ignore 'All' option
    if filters['school_class'] and filters['school_class'] != 'all':
        students = students.filter(school_class__name=filters['school_class'])
    if filters['stream'] and filters['stream'] != 'all':
        students = students.filter(stream__name=filters['stream'])
    if filters['section'] and filters['section'] != 'all':
        students = students.filter(section=filters['section'])
    if filters['status'] and filters['status'] != 'all':
        students = students.filter(status=filters['status'])



    # Get available classes and streams for the dropdowns
    school_classes = SchoolClass.objects.all()
    streams = Stream.objects.all().distinct()

    unique_streams = streams.values('name').distinct()

    return render(request, 'students/studentlist.html', {
        'students': students,
        'school_classes': school_classes,
        'streams': unique_streams,
        'filters': filters,  # Pass filters back to the template to maintain selection state
    })
    
def student_list(request):
    qs = Student.objects.select_related('school_class', 'stream') \
                        .order_by('admission_number')

    data = []
    for s in qs:
        data.append({
            'id':               s.id,
            'admission_number': s.admission_number,
            'schoolpay_code':   s.schoolpay_code,
            'first_name':       s.first_name,
            'other_names':      s.other_names,
            'date_of_birth':    s.date_of_birth.isoformat(),
            'gender':           s.gender,
            'school_class':     s.school_class.name if s.school_class else None,
            'stream':           s.stream.name if s.stream else None,
            'enrollment_date':  s.enrollment_date.isoformat(),
            'status':           s.status,
            'section':          s.section,
            'address':          s.address,
            # revert photo to just the relative path
            'photo':            s.photo.name if s.photo else None,
        })

    return JsonResponse(data, safe=False)


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:student_profile', pk=student.pk)
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {
        'form': form,
        'student': student,
        'is_edit': True
    })


# Delete Student View
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('students:studentDetails') 



 
# dashboards starthere   
 
def EnrolmentSummary(request):

    active_qs = Student.objects.filter(status='active')
    context = {
        'total_enrolment':    active_qs.count(),
        'male_count':         active_qs.filter(gender='male').count(),
        'female_count':       active_qs.filter(gender='female').count(),
        'boarding_count':     active_qs.filter(section='boarding').count(),
    }
    return render(request, 'students/Enrolmentsummary.html', context)


def class_gender_statistics_data(request):
    qs = Student.objects.filter(status='active')
    stats = (
        qs
        .values('school_class__name')
        .annotate(
            male=Count('id', filter=Q(gender='male')),
            female=Count('id', filter=Q(gender='female'))
        )
        .order_by('school_class__name')
    )
    labels        = [item['school_class__name'] for item in stats]
    male_counts   = [item['male'] for item in stats]
    female_counts = [item['female'] for item in stats]
    return JsonResponse({
        'labels':        labels,
        'male_counts':   male_counts,
        'female_counts': female_counts
    })
    
    
    # excel
def upload_students_excel_json(request):
    excel_file = request.FILES.get('excel_file')
    if not excel_file:
        return JsonResponse(
            {'success': False, 'errors': ['No file was uploaded.'], 'imported': 0, 'total': 0},
            status=400
        )
    _set_current_user(request.user)
    try:
        result = import_students_from_excel(excel_file)

        # If importer returns a tuple, unpack it.
        if isinstance(result, tuple) and len(result) == 3:
            imported, total, errors = result
            if errors:
                return JsonResponse({
                    'success': False,
                    'imported': imported,
                    'total': total,
                    'errors': errors
                }, status=200)
            return JsonResponse({
                'success': True,
                'imported': imported,
                'total': total,
                'message': f"Imported {imported} students successfully."
            }, status=200)

        # If importer returned a string (message), treat as full success:
        message = str(result)
        return JsonResponse({'success': True, 'message': message}, status=200)

    except Exception as e:
        # Catch any exception and split on “; ” to build an errors list
        msg = str(e)
        errs = msg.split('; ')
        return JsonResponse({
            'success': False,
            'errors': errs,
            'imported': 0,
            'total': 0
        }, status=200)
    


def load_streams(request):
    school_class_id = request.GET.get('school_class')
    if school_class_id:
        streams = Stream.objects.filter(school_class_id=school_class_id).order_by('name')
    else:
        streams = Stream.objects.none()
    stream_data = [{'id': s.id, 'name': s.name} for s in streams]
    return JsonResponse(stream_data, safe=False)

def get_student_info(request):
    admission_number = request.GET.get('admission_number', '').strip()
    try:
        student = Student.objects.get(admission_number__iexact=admission_number)
        return JsonResponse({
            'status': 'ok',
            'first_name': student.first_name,
            'other_names': student.other_names or '',
            'id': student.id,
            'photo_url': student.photo.url if student.photo else '',
            'status': student.status,
            'gender': student.gender
        })
    except Student.DoesNotExist:
        return JsonResponse({'status': 'not_found'})
    


def studentProfile(request, pk):
        student = get_object_or_404(Student.objects.select_related('school_class', 'stream'), pk=pk)
        return render(request, 'students/studentProfile.html', {
                    'student': student,
                    })

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:studentDetails')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {'form': form, 'student': student})

@require_POST
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:studentDetails')

