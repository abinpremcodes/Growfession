
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, DeveloperProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)

    fieldsets = UserAdmin.fieldsets + (
        ("Growfession Profile", {"fields": ("role",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Growfession Profile", {"fields": ("role",)}),
    )


@admin.register(DeveloperProfile)
class DeveloperProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "headline",
        "location",
        "is_public",
        "created_at",
    )

    list_filter = ("is_public", "created_at")

    search_fields = (
        "user__username",
        "user__email",
        "headline",
        "skills",
    )

    readonly_fields = ("created_at", "updated_at")

    ordering = ("-created_at",)
