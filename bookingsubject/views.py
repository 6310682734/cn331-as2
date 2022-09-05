from cgitb import small
from django.shortcuts import render
from .models import Subject
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.


def index(req, data={"status": None, "message": None}):
    subjects = Subject.objects.all()
    return render(req, "bookingsubject/index.html", {
        "subjects": subjects,
        "message": data["message"],
        "status": data["status"]
    })


def remove_subject(req, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
        subject.delete()
    except:
        return index(req, {"status": False, "message": "Delete fail"})
    return index(req, {"status": True, "message": "Remove subject successfully"})


def subject_info(req, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
        students = User.objects.filter(~Q(username="admin"))
        print("Students : ", students)
        return render(req, "bookingsubject/subject_info.html", {"subject_data": subject, "students": students})
    except:
        return index(req, {"status": False, "message": "Subject not Found"})
    return index(req)


def update_subject(req, subject_id):
    pass


def book_subject(req, subject_id):
    pass


def unbook_subject(req, subject_id):
    pass


def create_subject(req):
    if (req.method == "POST"):
        code = req.POST["code"]
        subject_name = req.POST["subject_name"]
        semester = req.POST["semester"]
        academic_year = req.POST["academic_year"]
        amount = req.POST["amount"]
        status = req.POST["status"]
        print(code, subject_name, semester, academic_year, amount, status)
        try:
            subjects = Subject.objects.get(code=code)
            return render(req, "bookingsubject/create_subject.html", {"message": "Code duplicate"})
        except:
            pass
        if (academic_year == ""):
            return render(req, "bookingsubject/create_subject.html", {"message": "Invalid input"})
        subject = Subject.objects.create(
            code=code,
            subject_name=subject_name,
            semester=semester,
            academic_year=academic_year,
            amount=amount,
            status=(True if status == "1" else False)
        )
        return index(req)
    else:
        return render(req, "bookingsubject/create_subject.html")
