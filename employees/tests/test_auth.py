# employees/tests/test_auth.py

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestAuth:

    def test_jwt_login(self, create_user):
        create_user()  
        client = APIClient()
        response = client.post('/api/token/', {
            'username': 'admin',
            'password': 'admin123'
        }, format='json')
        assert response.status_code == 200
        assert 'access' in response.data
