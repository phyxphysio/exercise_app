import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_success_page():
    client = Client()
    path = reverse("success")
    response = client.get(path)
    assert response.status_code == 200
