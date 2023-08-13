from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.item1 = MenuItem.objects.create(
            title="Pizza", price=200, inventory=50)
        self.item2 = MenuItem.objects.create(
            title="Burger", price=100, inventory=30)
        self.valid_payload = {
            'title': 'Spaghetti',
            'price': 150,
            'inventory': 20
        }
        # Assuming you named your url 'menu-items-list'
        self.url = reverse('menu-items-list')

    def test_get_all_menu_items(self):
        response = self.client.get(self.url)
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
