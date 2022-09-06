from django.contrib import admin

# Register your models here.

from .models import Subject, Enrollment


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("code", "subject_name", "semester",
                    "academic_year", "amount", "status")


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("username", "subject_id")


admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Subject, SubjectAdmin)
