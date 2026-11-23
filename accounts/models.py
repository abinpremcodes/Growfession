
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        DEVELOPER = "DEVELOPER", "Developer"
        RECRUITER = "RECRUITER", "Recruiter"
        MENTOR = "MENTOR", "Mentor"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.DEVELOPER,
    )

    def __str__(self):
        return self.username


class DeveloperProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="developer_profile",
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True,
    )

    headline = models.CharField(
        max_length=150,
        blank=True,
    )

    bio = models.TextField(blank=True)

    location = models.CharField(
        max_length=100,
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    skills = models.TextField(
        blank=True,
        help_text="Enter your skills separated by commas.",
    )

    education = models.TextField(blank=True)

    experience = models.TextField(blank=True)

    github_url = models.URLField(blank=True)

    linkedin_url = models.URLField(blank=True)

    portfolio_url = models.URLField(blank=True)

    is_public = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
