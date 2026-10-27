from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        DEVELOPER="DEVELOPER","Developer"
        RECRUITER="RECRUITER","Recruiter"
        MENTOR="MENTOR","Mentor"

    role=models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.DEVELOPER,
    )

    def __str__(self):
        return self.username



        
        

