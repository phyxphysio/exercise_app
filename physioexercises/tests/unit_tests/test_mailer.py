import pytest
from django.urls import reverse
from django.core import mail
from django.test import RequestFactory
from django.contrib.sessions.backends.db import SessionStore
from exercises.views import send_email  # Adjust the import path as necessary
from exercises.forms import EmailForm  # Assuming this is the form used in your view
from exercises.models import Exercise

# Helper function to add session to request
def add_session_to_request(request,):
    # Instead of using SessionMiddleware, manually set up the session
    session = SessionStore()
    session.save()  # Saving the session to generate session_key
    request.session = session


@pytest.mark.django_db
def test_send_email_view_get_request(client, test_user):
    # Log in the test user
    client.force_login(test_user)

    # Setup an Exercise instance for the session
    exercise = Exercise.objects.create(name="Test Exercise", link="http://example.com")
    
    # Define the URL for the GET request
    url = reverse("send_email")

    # Setup session data
    session = client.session
    session["message"] = {
        "patient_name": "John Doe",
        "frequency": "daily",
        "sets": 3,
        "reps": 10,
        "next_appointment": "2024-02-28",
        "exercises": [exercise.id],  # Assuming your view expects IDs in the session
        "patient_email": "patient@example.com",
    }
    session.save()

    # Make the GET request to the send_email view
    response = client.get(url)

    # Assertions
    assert response.status_code == 200  # Expecting a 200 OK response

@pytest.mark.django_db
def test_send_email_view_post_request(client, test_user):
    # Log in the test user
    client.force_login(test_user)

    # Define the URL and data for the POST request
    url = reverse("send_email")
    data = {
        "subject": "Test Subject",
        "message": "This is a test message.",
        "recipient_list": ["recipient@example.com"],  # recipient_list should typically be a list
    }
    
    # Setup session data if needed
    session = client.session
    session["message"] = {
        "patient_name": "John Doe",
        "frequency": "daily",
        "sets": 3,
        "reps": 10,
        "next_appointment": "2024-02-28",
        "exercises": 1,
        "patient_email": "patient@example.com",
    }
    session.save()

    # Make the POST request to the send_email view
    response = client.post(url, data)

    # Assertions
    assert response.status_code == 302  # Expecting a redirect on successful form submission

    # Verify an email was sent
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == "Test Subject"
