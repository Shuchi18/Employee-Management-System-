import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_employee_list(api_client_with_token):
    url = reverse('employee-list')
    response = api_client_with_token.get(url)
    assert response.status_code == 200
