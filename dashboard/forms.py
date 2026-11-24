
from django import forms

from .models import Project, Task, LearningGoal


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


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            "title",
            "description",
            "priority",
            "status",
            "due_date",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter your task title",
            }),

            "description": forms.Textarea(attrs={
                "placeholder": "Describe what you need to do",
                "rows": 4,
            }),

            "priority": forms.Select(),

            "status": forms.Select(),

            "due_date": forms.DateInput(attrs={
                "type": "date",
            }),
        }


class LearningGoalForm(forms.ModelForm):

    class Meta:
        model = LearningGoal

        fields = [
            "title",
            "description",
            "target_date",
            "progress",
            "status",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "e.g. Learn Django REST Framework",
            }),

            "description": forms.Textarea(attrs={
                "placeholder": "Describe what you want to learn",
                "rows": 4,
            }),

            "target_date": forms.DateInput(attrs={
                "type": "date",
            }),

            "progress": forms.NumberInput(attrs={
                "min": 0,
                "max": 100,
                "placeholder": "0 - 100",
            }),

            "status": forms.Select(),
        }
