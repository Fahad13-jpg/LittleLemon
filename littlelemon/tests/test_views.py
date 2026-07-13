from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from LittleLemonAPI.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        MenuItem.objects.create(Title="Pizza", Price=20, Inventory=10)
        MenuItem.objects.create(Title="Burger", Price=15, Inventory=5)

    def test_getall(self):
        client = APIClient()

        response = client.get('/restaurant/menu/')

        items = MenuItem.objects.all()
        serializer = MenuSerializer(items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)