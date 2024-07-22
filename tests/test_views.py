from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        # Añadir instancias de prueba del modelo Menu
        self.client = APIClient()
        Menu.objects.create(title='Pasta', price=12.99, inventory=10)
        Menu.objects.create(title='Pizza', price=9.99, inventory=20)
        Menu.objects.create(title='Salad', price=7.99, inventory=30)

    def test_getall(self):
        # Recuperar todos los objetos Menu
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Comprobar si los datos serializados son iguales a la respuesta
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data), serializer.data)