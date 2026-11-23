
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, DeveloperProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    role = forms.ChoiceField(
        choices=User.Role.choices,
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "role", "password1", "password2"]


class DeveloperProfileForm(forms.ModelForm):

    class Meta:
        model = DeveloperProfile
        exclude = ["user", "created_at", "updated_at"]

        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
            "skills": forms.Textarea(attrs={"rows": 3}),
            "education": forms.Textarea(attrs={"rows": 3}),
            "experience": forms.Textarea(attrs={"rows": 3}),
        }
