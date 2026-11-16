from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    role=forms.ChoiceField(
        choices=User.Role.choices,
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "role", "password1", "password2"]