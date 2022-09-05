from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='booking_index'),
    path('create', views.create_subject, name="create_subject"),
    path("<int:subject_id>", views.index, name="subject_list"),
    path("<int:subject_id>/book", views.book_subject, name="book_subject"),
    path("<int:subject_id>/unbook", views.unbook_subject, name="unbook_subject")
]
