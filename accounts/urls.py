
from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path(
        "developer/profile/",
        views.developer_profile_view,
        name="developer_profile",
    ),
]
