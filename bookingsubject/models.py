from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.


class Subject(models.Model):
    id = models.CharField(max_length=25, blank=False,
                          null=False, unique=True, primary_key=True)
    code = models.CharField(max_length=3)
    subject_name = models.CharField(max_length=15)
    semester = models.CharField(max_length=1)
    academic_year = models.IntegerField()
    amount = models.IntegerField()
    status = models.BooleanField()
    student = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.code} {self.subject_name} {self.semester} {self.academic_year} {self.amount} {self.status} {self.student}"


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="id")
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, to_field="id", unique=True)
    # firstname = models.CharField(max_length=20)
    # lastname = models.CharField(max_length=20)
    # student_id = models.CharField(max_length=10)
    # password = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user} {self.subject}"
