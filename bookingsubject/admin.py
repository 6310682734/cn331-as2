from django.contrib import admin

# Register your models here.

from .models import Subject, Student


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("code", "subject_name", "semester",
                    "academic_year", "amount", "status")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "student_id")


admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
