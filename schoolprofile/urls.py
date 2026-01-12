from django.urls import path
from .views import school_profile, edit_school_profile
from . import views
from .views_subject import list_subjects, add_subject, edit_subject, delete_subject, assign_subjects_to_class

app_name = "profile"

urlpatterns = [
    path("", school_profile, name="school_profile"),
    path("edit/", edit_school_profile, name="edit_school_profile"),

        # ============================
    #          LEVELS
    # ============================
    path("levels/", views.list_levels, name="list_levels"),
    path("levels/<int:level_id>/edit/", views.edit_level, name="edit_level"),
    path("levels/<int:level_id>/delete/", views.delete_level, name="delete_level"),

    # ============================
    #          CLASSES
    # ============================
    path("classes/", views.list_classes, name="list_classes"),
    path("classes/<int:class_id>/edit/", views.edit_class, name="edit_class"),
    path("classes/<int:class_id>/delete/", views.delete_class, name="delete_class"),

    # ============================
    #          STREAMS
    # ============================
    path("streams/", views.list_streams, name="list_streams"),
    path("streams/<int:stream_id>/edit/", views.edit_stream, name="edit_stream"),
    path("streams/<int:stream_id>/delete/", views.delete_stream, name="delete_stream"),

    # SUBJECTS
    path("subjects/", list_subjects, name="list_subjects"),
    path("subjects/add/", add_subject, name="add_subject"),
    path("subjects/<int:subject_id>/edit/", edit_subject, name="edit_subject"),
    path("subjects/<int:subject_id>/delete/", delete_subject, name="delete_subject"),
    path("classes/<int:class_id>/assign-subjects/", assign_subjects_to_class, name="assign_subjects_to_class"),
]
