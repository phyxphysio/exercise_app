import pytest
from django.contrib.auth.models import User

@pytest.fixture
def test_user(db):
    user = User.objects.create_user(username='testuser', password='12345')
    return user
