
from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            "title",
            "description",
            "tech_stack",
            "status",
            "live_url",
            "github_url",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter your project name",
            }),

            "description": forms.Textarea(attrs={
                "placeholder": "Describe what your project does",
                "rows": 4,
            }),

            "tech_stack": forms.TextInput(attrs={
                "placeholder": "Python, Django, PostgreSQL",
            }),

            "status": forms.Select(),

            "live_url": forms.URLInput(attrs={
                "placeholder": "https://your-project.com",
            }),

            "github_url": forms.URLInput(attrs={
                "placeholder": "https://github.com/username/project",
            }),
        }
