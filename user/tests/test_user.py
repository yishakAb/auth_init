from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

CREATE_USER = reverse('user:create')


class UserCreateApiTests(TestCase):
    """Test user creation."""

    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        """Test creating a user."""

        data = {
            'name': 'User name',
            'email': 'test@test.com',
            'password': 'test123'
        }

        res = self.client.post(CREATE_USER, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
