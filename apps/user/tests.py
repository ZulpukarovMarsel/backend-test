from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('sign_up')
        self.signin_url = reverse('sign_in')
        self.logout_url = reverse('sign_out')
        self.user_data = {'email': 'testmars@example.com', 'password': 'testpassword'}
        self.user = User.objects.create_user(email=self.user_data['email'], password=self.user_data['password'])

    def test_signup(self):
        User.objects.filter(email=self.user_data['email']).delete()
        response = self.client.post(self.signup_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin(self):
        response = self.client.post(self.signin_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_logout(self):
        response = self.client.post(self.signin_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data['access']
        response = self.client.post(self.logout_url, {'refresh': token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
