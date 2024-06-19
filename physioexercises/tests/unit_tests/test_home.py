import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_protected_view_loads_for_logged_in_user(client, test_user):
    client.login(username="testuser", password="12345")  # Log the user in

    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
