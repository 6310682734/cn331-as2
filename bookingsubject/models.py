from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.


class Subject(models.Model):
    code = models.CharField(max_length=3)
    subject_name = models.CharField(max_length=15)
    semester = models.CharField(max_length=1)
    academic_year = models.IntegerField()
    amount = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f"{self.code} {self.subject_name} {self.semester} {self.academic_year} {self.amount} {self.status}"


class Enrollment(models.Model):
    username = models.CharField(max_length=10)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    # firstname = models.CharField(max_length=20)
    # lastname = models.CharField(max_length=20)
    # student_id = models.CharField(max_length=10)
    # password = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user_id} {self.username} {self.subject_id}"
