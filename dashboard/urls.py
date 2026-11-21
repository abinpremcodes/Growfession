

from django.urls import path
from . import views

urlpatterns = [
    path("developer/", views.developer_dashboard, name="developer_dashboard"),
    path("recruiter/", views.recruiter_dashboard, name="recruiter_dashboard"),
    path("mentor/", views.mentor_dashboard, name="mentor_dashboard"),

    path("projects/", views.project_list, name="project_list"),
    path("projects/create/", views.project_create, name="project_create"),
    path("projects/<int:project_id>/edit/", views.project_edit, name="project_edit"),
    path("projects/<int:project_id>/delete/", views.project_delete, name="project_delete"),
]
