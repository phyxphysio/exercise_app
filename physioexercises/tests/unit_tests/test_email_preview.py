import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_email_preview():
    client = Client()
    path = reverse('send_email')
    response = client.get(path)
    assert response.status_code == 302
