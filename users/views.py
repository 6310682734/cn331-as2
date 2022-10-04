
from django.shortcuts import render
# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


def index(req):
    return render(req, "users/index.html")


def register_view(req):
    obj = {
        "status": True,
        "message": ""
    }
    if req.method == "POST":
        username = req.POST["username"]
        firstname = req.POST["firstname"]
        lastname = req.POST["lastname"]
        password = req.POST["password"]
        email = req.POST["email"]
        con_password = req.POST["confirm_password"]
        try:
            _user = User.objects.get(username=username)
            return render(req, "users/register.html", {"status": False, "message": "Username already used"}, status=400)
        except:
            pass
            # print("<--- User not found (Can register) --->")
        if (con_password != password):
            obj['status'] = False
            obj["message"] = "Confirm password fail"
        if (username == "" or len(username) == 0 or password == "" or con_password == "" or email == ""):
            obj["status"] = False
            obj["message"] = "Enter your information"
        # Register Process
        if (obj["status"]):
            obj['message'] = "Register successfully"
            user = User.objects.create_user(
                username=username, password=password, email=email, first_name=firstname, last_name=lastname)
            return render(req, "users/register.html", {"status": True, "message": obj["message"]}, status=200)
        else:
            return render(req, "users/register.html", {"status": False, "message": obj["message"]}, status=400)
    return render(req, "users/register.html", obj, status=200)


def login_view(req):
    if (req.method == "POST"):
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req, username=username, password=password)
        if (user is not None):
            print("<-------  Login Success ----->")
            login(req, user)
            return render(req, "users/index.html", status=200)
            # return HttpResponseRedirect(reverse("index"))
        else:
            return render(req, "users/login.html", {"message": "Invalid credential"}, status=400)
    return render(req, "users/login.html")


def logout_view(req):
    logout(req)
    return render(req, "users/login.html", {"message": "Logged out"})
