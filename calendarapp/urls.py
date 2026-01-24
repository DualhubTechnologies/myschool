from django.urls import path
from . import views

app_name = "calendar"

urlpatterns = [

    # ------- Calendar UI -------
    path("calendar/", views.calendar_page, name="calendar"),
    path("events/", views.get_events, name="get_events"),
    path("events/add/", views.add_event, name="add_event"),

    # ------- Academic Years -------
    path("years/", views.list_academic_years, name="list_academic_years"),

    # ------- School Terms -------
    path("terms/", views.list_terms, name="list_terms"),
    path("terms/<int:term_id>/edit/", views.edit_term, name="edit_term"),
    path("terms/<int:term_id>/delete/", views.delete_term, name="delete_term"),


]
