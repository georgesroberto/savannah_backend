"""
Default views Configuration for savannah/orders
"""

from django.shortcuts import redirect

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer



# Login Redirect view
def login_redirect(request):
    return redirect('account_login')

def home(request):
    return redirect('customer-list-create')

# Customer Views
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


# Order Views
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
