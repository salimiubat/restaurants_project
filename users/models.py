# models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone




class UserTypes(models.TextChoices):

    EMPLOYEE = " EMPLOYEE", " Employee"
    OWNER = "OWNER", "Owner"





class User(AbstractUser):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    role = models.CharField(max_length=20, choices=UserTypes.choices, default=UserTypes.EMPLOYEE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone_number"] #any kind of field
    def __str__(self):
        return self.username
