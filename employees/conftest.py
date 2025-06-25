# conftest.py

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def create_user(db):
    def make_user(username='admin', password='admin123'):
        return User.objects.create_user(username=username, password=password)
    return make_user


@pytest.fixture
def get_token(create_user):
    def generate_token():
        user = create_user()
        client = APIClient()
        response = client.post('/api/token/', {
            'username': user.username,
            'password': 'admin123'
        }, format='json')
        return response.data['access']
    return generate_token


@pytest.fixture
def api_client_with_token(get_token):
    token = get_token()
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return client
