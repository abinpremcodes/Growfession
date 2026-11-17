
from django.urls import path
from . import views

urlpatterns = [ 
    path("developer/", views.developer_dashboard, name="developer_dashboard"),
    path("recruiter/", views.recruiter_dashboard, name="recruiter_dashboard"),
    path("mentor/", views.mentor_dashboard, name="mentor_dashboard"),
]
    

