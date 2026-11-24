
from django.contrib import admin
from .models import Project, Task, LearningGoal


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("title", "description", "user__username")
    ordering = ("-created_at",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "priority",
        "status",
        "due_date",
        "created_at",
    )

    list_filter = (
        "priority",
        "status",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "user__username",
    )

    ordering = ("due_date", "-created_at")


@admin.register(LearningGoal)
class LearningGoalAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "progress",
        "status",
        "target_date",
        "created_at",
    )

    list_filter = (
        "status",
        "target_date",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "user__username",
    )

    ordering = ("target_date", "-created_at")
