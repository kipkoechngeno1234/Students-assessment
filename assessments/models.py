from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Assessment(models.Model):
    title = models.CharField(max_length=180)
    questions = models.TextField()
    correct_answers = models.CharField(max_length=200)
    created_at = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Submission(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    answers = models.CharField(max_length=350)
    score = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)