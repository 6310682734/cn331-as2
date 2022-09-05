from django.shortcuts import render
from .models import Subject


# Create your views here.
def index(req):
    subjects = Subject.objects.all()
    print("Subjects : ", subjects)
    return render(req, "bookingsubject/index.html", {
        "subjects": subjects
    })
