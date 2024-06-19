# tests.py
import pytest
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User
from mixer.backend.django import mixer
from .views import preview_activation_email

@pytest.mark.django_db
def test_preview_activation_email():
    # Arrange
    user = mixer.blend(User)
    request = RequestFactory().get(reverse('preview_activation'))
    request.user = user
    
    # Act
    response = preview_activation_email(request)

    # Assert
    assert response.status_code == 200
    context = response.content.decode('utf-8')
    assert "Physiotherapist Name" in context
    assert "https://physioward.com.au/book-now/" in context
    assert "https://physioward.com.au/wp-content/uploads/2022/09/physioward-secondary-logo-stacked-left-full-color-rgb.svg" in context
    assert "Patient name" in context
