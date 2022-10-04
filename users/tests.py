from audioop import reverse
from email import header
from urllib import response
from django.test import TestCase
from . import views
from django.contrib.auth.models import User
# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="admin", password="admin")

    def test_index_view(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get("/users/register")
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        url = "/users/register"
        body = {
            "username": "6310682718",
            "firstname": "Pongsakorn",
            "lastname": "Parsoppornpiboon",
            "password": "ter",
            "confirm_password": "ter1",
            "email": "6310682718@student.tu.ac.th"
        }
        # with success case
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, 400)  # confirm password fail
        # confirm pass fail
        body["confirm_password"] = "ter"  # with correct password
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get("/users/login")
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        url = "/users/login"
        body = {"username": "admin", "password": "admin1"}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, 400)  # Incorrect Password
        body["password"] = "admin"
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, 200)  # Correct Password
        # Test login

    def test_logout_view(self):
        response = self.client.get("/users/logout")
        self.assertEqual(response.status_code, 200)
