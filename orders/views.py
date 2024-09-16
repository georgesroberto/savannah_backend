"""
Default views Configuration for savannah/orders
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import generics

from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from .utils import send_sms

@receiver(post_save, sender=Order)
def send_order_sms(sender, instance, created, **kwargs):
    if created:
        customer_phone = instance.customer.phone
        message = f"New order created: Item - {instance.item}, Amount - {instance.amount}"
        send_sms(customer_phone, message)


# Customer Views
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Order Views
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
