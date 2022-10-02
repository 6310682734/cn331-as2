from cgitb import small
import code
from itertools import count
from this import s
from unicodedata import name
from django.shortcuts import render
from .models import Enrollment, Subject
from django.db.models import Q
from django.contrib.auth.models import User
from django import template

register = template.Library()

# Create your views here.


def index(req, data={"status": None, "message": None}):
    subjects = Subject.objects.all()
    return render(req, "bookingsubject/index.html", {
        "subjects": subjects,
        "message": data["message"],
        "status": data["status"]
    })


def enrollmented(req):
    try:
        user_data = User.objects.get(id=req.user.id)
        enrollment = Enrollment.objects.filter(user=user_data)
        if (enrollment.count() <= 0):
            return render(req, "bookingsubject/enrollment_info.html", {"enrolls": {}})
        #student = User.objects.filter(is_superuser=False, is_staff=False, is_active=True)
        print(enrollment)
        return render(req, "bookingsubject/enrollment_info.html", {"enrolls": enrollment})
    except Exception as e:
        print("Error : ", e)
        return index(req, {"status": False, "message": "Something went wrong"})


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
        #student = User.objects.filter(is_superuser=False, is_staff=False, is_active=True)
        check_enroll = is_already_enroll(req.user.id, subject_id)
        enrollment_list = Enrollment.objects.filter(subject=subject)
        return render(req, "bookingsubject/subject_info.html", {"subject_data": subject, "enrolls": enrollment_list, "is_already_enroll": check_enroll})
    except Exception as e:
        print("Error : ", e)
        return index(req, {"status": False, "message": "Something went wrong"})


def update_subject(req, subject_id):
    if (req.method == "POST"):
        code = req.POST["code"]
        subject_name = req.POST["subject_name"]
        semester = req.POST["semester"]
        academic_year = req.POST["academic_year"]
        amount = req.POST["amount"]
        status = req.POST["status"]
        try:
            subjects = Subject.objects.get(code=code)
            return render(req, "bookingsubject/update_subject.html", {"message": "Code duplicate"})
        except:
            pass
        if (academic_year == ""):
            return render(req, "bookingsubject/update_subject.html", {"message": "Invalid input"})
        subject = Subject.objects.filter(id=subject_id).update(
            code=code,
            subject_name=subject_name,
            semester=semester,
            academic_year=academic_year,
            amount=amount,
            status=status
        )
        return index(req)
    else:
        subject_data = Subject.objects.get(id=subject_id)
        return render(req, "bookingsubject/update_subject.html", {"subject_data": subject_data})


def is_already_enroll(user_id, subject_id=None):
    try:
        user_data = User.objects.get(id=user_id)
        if (subject_id == None):
            enroll = Enrollment.objects.get(user=user_data)
            return True
        else:
            subject_data = Subject.objects.get(id=subject_id)
            print(subject_data)
            enroll = Enrollment.objects.get(
                user=user_data, subject=subject_data)
            return True
    except:
        return False


def enroll_subject(req, subject_id, user_id):
    if (req.method == "POST"):
        user_data = User.objects.get(id=user_id)
        username = user_data.username
        subject_data = Subject.objects.get(id=subject_id)
        if (is_already_enroll(user_id, subject_id)):
            return index(req, {"status": False, "message": "Already Enroll"})
        if (subject_data.student >= subject_data.amount):
            return index(req, {"status": False, "message": "Out of seat"})
        enroll = Enrollment.objects.create(
            user=user_data,
            subject=subject_data
        )
        subject_data.student += 1
        subject_data.save()
        return index(req, {"status": True, "message": "Enroll subject successfully"})
    else:
        return index(req, {"status": True, "message": "Enroll subject failed"})


def unenroll_subject(req, subject_id):
    try:
        user_data = User.objects.get(id=req.user.id)
        subject_data = Subject.objects.get(id=subject_id)
        enroll = Enrollment.objects.get(user=user_data, subject=subject_data)
        enroll.delete()
        subject_data.student -= 1
        subject_data.save()
        return index(req, {"status": True, "message": "Unenroll successfully"})
    except Exception as e:
        print("Error : ", e)
        return index(req, {"status": False, "message": "Delete fail"})


def create_subject(req):
    if (req.method == "POST"):
        code = req.POST["code"]
        subject_name = req.POST["subject_name"]
        semester = req.POST["semester"]
        academic_year = req.POST["academic_year"]
        amount = req.POST["amount"]
        status = req.POST["status"]
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
