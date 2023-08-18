from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from restaurant.models import Menu
from django.contrib.auth.models import User
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='1234567889')  # Use get instead of filter
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        self.menu_item1 = Menu.objects.create(title="Item1", price=10, inventory=50)
        self.menu_item2 = Menu.objects.create(title="Item2", price=15, inventory=30)

    def test_getall(self):
        url = reverse('menu-list')  # Use the name of the URL as defined in your project's URLs
        response = self.client.get(url)

        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

