from django.test import TestCase
from rest_framework.test import APIClient
from .models import MenuItem


class MenuItemsViewTestCase(TestCase):

    def setUp(self):
        # Create a sample menu item for testing
        self.menu_item = MenuItem.objects.create(
            title="Test Item", price=5.00, inventory=10)
        self.client = APIClient()

    def test_get_menu_items(self):
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
