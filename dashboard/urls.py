
from django.urls import path
from . import views

urlpatterns = [
    path("developer/", views.developer_dashboard, name="developer_dashboard"),
    path("recruiter/", views.recruiter_dashboard, name="recruiter_dashboard"),
    path("mentor/", views.mentor_dashboard, name="mentor_dashboard"),

    # Project URLs
    path("projects/", views.project_list, name="project_list"),
    path("projects/create/", views.project_create, name="project_create"),
    path("projects/<int:project_id>/edit/", views.project_edit, name="project_edit"),
    path("projects/<int:project_id>/delete/", views.project_delete, name="project_delete"),

    # Task URLs
    path("tasks/", views.task_list, name="task_list"),
    path("tasks/create/", views.task_create, name="task_create"),
    path("tasks/<int:task_id>/edit/", views.task_edit, name="task_edit"),
    path("tasks/<int:task_id>/delete/", views.task_delete, name="task_delete"),

    #Learning goals URLs
    path("learning-goals/",views.learning_goal_list,  name="learning_goal_list"),
    path("learning-goals/create/",views.learning_goal_create, name="learning_goal_create"),
    path("learning-goals/<int:goal_id>/edit/", views.learning_goal_edit, name="learning_goal_edit"),
    path("learning-goals/<int:goal_id>/delete/", views.learning_goal_delete, name="learning_goal_delete"),


        
       

]
