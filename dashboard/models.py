from django.db import models
from django.conf import settings
class Project(models.Model):

    class Status(models.TextChoices):
        NOT_STARTED="NOT_STARTED","Not Started"
        IN_PROGRESS="IN_PROGRESS","In Progress"
        COMPLETED="COMPLETED","Completed"

    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects"
    
    )

    title=models.CharField(max_length=150)

    description=models.TextField()

    tech_stack=models.CharField(max_length=255)

    status=models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NOT_STARTED)

    live_url=models.URLField(blank=True)

    github_url=models.URLField(blank=True)

    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title






