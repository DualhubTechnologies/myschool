from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (addstudent, class_gender_statistics_data, get_student_info, load_streams, student_list, studentProfile,
                    student_edit,student_delete,
                    edit_student, delete_student, studentDetails,  upload_students_excel_json)
from .views import EnrolmentSummary 

app_name = "students"

urlpatterns = [
    path('add/', addstudent, name='addstudent'),
    path('studentDetails/', studentDetails, name='studentDetails'),
    path('list/', student_list, name='list'),
    path('students/<int:pk>/edit/', student_edit, name='student_edit'),
    path('delete_student/<int:id>/', delete_student, name='delete_student'),

    path('edit_parent/<int:id>/', edit_student, name='edit_parent'),
    path('delete_Parent/<int:id>/', delete_student, name='delete_Parent'),
    path('api/student-info/', get_student_info, name='get_student_info'),
    
    # excel upload
    path('ajax/load-streams/', load_streams, name='ajax_load_streams'),


    path('api/upload-excel/', upload_students_excel_json, name='upload_students_excel_json'),
    
    # dashboards
    path('enrollment-summary/', EnrolmentSummary, name='enrollment-summary'),
    path('api/class-gender-stats/', class_gender_statistics_data, name='class-gender-stats'),



    # student controls
    path('students/<int:pk>/', studentProfile, name='student_profile'),
    path('students/<int:pk>/edit/', student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', student_delete, name='student_delete'),
]

# Add static route to serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)