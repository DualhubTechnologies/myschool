from django.urls import path
from . import views


app_name = "teachers"

urlpatterns = [
    path("list/", views.list_staff, name="list_staff"),
    path("create/", views.create_staff, name="create_staff"),
    path("edit/<int:staff_id>/", views.edit_staff, name="edit_staff"),
    path("delete/<int:staff_id>/", views.delete_staff, name="delete_staff"),
]



