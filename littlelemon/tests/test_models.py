from django.test import TestCase
from restaurant.models import MenuItem

class MenuTest(TestCase):
    def test_get_items(self):
        item = MenuItem.objects.create(title='Test Item', price=10.99, inventory=5)
        self.assertEqual(str(item), 'Test Item : 10.99')
        