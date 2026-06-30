from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    ADMIN = "admin"
    STUDENT = "student"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (STUDENT, "Student"),
    ]

    Email = models.EmailField(unique=True)
    
    role = models.CharField(max_length=25, choices=ROLE_CHOICES, default=STUDENT)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email