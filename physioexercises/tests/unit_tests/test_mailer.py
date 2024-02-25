import pytest
from django.urls import reverse
from django.core import mail
from django.test import RequestFactory
from django.contrib.sessions.backends.db import SessionStore
from exercises.views import send_email  # Adjust the import path as necessary
from exercises.forms import EmailForm  # Assuming this is the form used in your view
from exercises.models import Exercise

# Helper function to add session to request
def add_session_to_request(request):
    # Instead of using SessionMiddleware, manually set up the session
    session = SessionStore()
    session.save()  # Saving the session to generate session_key
    request.session = session


@pytest.mark.django_db
def test_send_email_view_get_request(rf, mocker):
    # Setup request with session data
    request = rf.get(reverse("send_email"))
    exercise = Exercise.objects.create(name="Test Exercise", link="http://example.com")

    add_session_to_request(request)
    request.session["message"] = {
        "patient_name": "John Doe",
        "frequency": "daily",
        "sets": 3,
        "reps": 10,
        "next_appointment": "2024-02-28",
        "exercises": [1],
        "patient_email": "patient@example.com",
    }

    response = send_email(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_send_email_view_post_request(rf, mocker):

    # Setup request with session data
    request = rf.post(
        reverse("send_email"),
        {
            "subject": "Test Subject",
            "message": "This is a test message.",
            "recipient_list": "recipient@example.com",
        },
    )
    add_session_to_request(request)
    request.session["message"] = {
        "patient_name": "John Doe",
        "frequency": "daily",
        "sets": 3,
        "reps": 10,
        "next_appointment": "2024-02-28",
        "exercises": 1,
        "patient_email": "patient@example.com",
    }

    response = send_email(request)
    assert (
        response.status_code == 302
    )  # Expecting a redirect on successful form submission

    # Verify send_mail was called
    assert (
        len(mail.outbox) == 1
    )  # Alternatively, check this if you want to inspect the sent email
    assert mail.outbox[0].subject == "Test Subject"
