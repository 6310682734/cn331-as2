from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='booking_index'),
    path('create', views.create_subject, name="create_subject"),
    path("<int:subject_id>/remove", views.remove_subject, name="remove_subject"),
    path("<int:subject_id>", views.subject_info, name="subject_info"),
    path("<int:subject_id>/<int:user_id>/enroll",
         views.enroll_subject, name="enroll_subject"),
    path("<int:subject_id>/unenroll",
         views.unenroll_subject, name="unenroll_subject")
]
