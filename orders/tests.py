"""
Default etst Configuration for savannah/orders
"""

from django.test import TestCase
from .models import Customer, Order
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


# Create your tests here.
class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='John Doe', code='CUST001', phone='+254701234567')

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, 'John Doe')
        self.assertEqual(self.customer.phone, '+254701234567')

class OrderModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='Jane Doe', code='CUST002', phone='+254701234568')
        self.order = Order.objects.create(customer=self.customer, item='Laptop', amount=1000)

    def test_order_creation(self):
        self.assertEqual(self.order.item, 'Laptop')
        self.assertEqual(self.order.amount, 1000)

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name='Jane Doe', code='CUST002', phone='+254701234568')

    def test_create_order(self):
        data = {
            'customer': self.customer.id,
            'item': 'Tablet',
            'amount': 500
        }
        response = self.client.post(reverse('order-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
