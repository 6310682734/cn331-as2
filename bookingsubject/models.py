from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms
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


class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    student_id = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.student_id} {self.password}"
