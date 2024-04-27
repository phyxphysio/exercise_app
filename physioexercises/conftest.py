import pytest
from django.contrib.auth.models import User
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), "../..", ".env.dev")
load_dotenv(dotenv_path=dotenv_path)


@pytest.fixture
def test_user(db):
    user = User.objects.create_user(username="testuser", password="12345")
    return user
