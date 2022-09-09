from django.contrib import admin

# Register your models here.

from .models import Subject, Enrollment


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("code", "subject_name", "semester",
                    "academic_year", "amount" ,"student" ,"status")


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("user", "subject")


admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Subject, SubjectAdmin)
