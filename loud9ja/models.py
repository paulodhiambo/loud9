from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    PLATFORM = [
        ("LOUD", "LOUD"),
        ("GOOGLE", "GOOGLE"),
        ("FACEBOOK", "FACEBOOK"),
        ("APPLE", "APPLE")
    ]
    GENDER = [
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        ("OTHER", "OTHER")
    ]
    email = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=GENDER, default="MALE")
    platform = models.CharField(max_length=30, choices=PLATFORM, default="LOUD")

    def __str__(self):
        return self.name
