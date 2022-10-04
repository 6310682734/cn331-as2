from urllib import response
from django.test import TestCase

from bookingsubject.models import Enrollment, Subject
from django.contrib.auth.models import User
# Create your tests here.


class EnrollmentTestCase(TestCase):
    def setUp(self):
        Subject.objects.create(code="TU100", subject_name="TU100",
                               semester=1, academic_year="2022", amount=1, status=True)
        User.objects.create(username="admin", password="admin")

    def test_seat_available(self):
        subject = Subject.objects.first()
        self.assertTrue(subject.is_seat_available())

    def test_enrollmented_view(self):
        url = "/bookingsubject/enrollmented"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_subject_info(self):
        url = "/bookingsubject/1"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_enroll_subject(self):
        url = "/bookingsubject/1/1/enroll"
        body = {"user_id": 1, "subject_id": 1}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, 200)  # Test enroll subject

        body["subject_id"] = 10
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, 400)  # Test enroll subject

        subject = Subject.objects.get(id=1)
        self.assertFalse(subject.is_seat_available())  # Test seat unavailable

    def test_unenroll_subject(self):
        url = "/users/login"
        body = {"username": "admin", "password": "admin"}
        response = self.client.post(url, body)
        subject_id = 0

        url = "/bookingsubject/1/1/enroll"
        body = {"user_id": 1, "subject_id": subject_id}
        response = self.client.post(url, body)

        url = f"/bookingsubject/{subject_id}/unenroll"
        body = {"subject_id": subject_id}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, 200)

        # body["subject_id"] = 10
        # response = self.client.post(url, body)
        # self.assertEqual(response.status_code, 400)  # Unknown Subject ID

    def test_remove_subject(self):

        url = "/bookingsubject/1/remove"
        body = {"subject_id": 1}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, 200)

        body["subject_id"] = 10
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, 400)  # Unknown Subject ID

    def test_update_subject(self):
        url = "/bookingsubject/1/update"
        body = {
            "subject_id": 1,
            "code": 100,
            "subject_name": "TU200",
            "semester": 2,
            "academic_year": 2022,
            "amount": 50,
            "status": 0,
        }
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, 200)

    # def test_enroll_subject(self):
    #     subject = Subject.objects.first()
    #     user1 = User.objects.create(username="6310682718")
    #     Enrollment.objects.create(user=user1, subject=subject)
    #     student = subject.student + 1
    #     Subject.objects.filter(
    #         pk=subject.pk).update(student=student)
    #     subject.refresh_from_db()
    #     self.assertTrue(subject.student == 1)
    #     self.assertFalse(subject.is_seat_available())
