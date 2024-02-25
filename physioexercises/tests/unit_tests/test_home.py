import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_home_page():
    client = Client()
    path = reverse('home')
    response = client.get(path)
    assert response.status_code == 200
