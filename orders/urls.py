"""
Default urls Configuration for savannah/orders
"""

from django.urls import path
from .views import (
    CustomerListCreateView,
    CustomerRetrieveUpdateDestroyView,
    OrderListCreateView,
    OrderRetrieveUpdateDestroyView
)

urlpatterns = [
    # Customer URLs
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),

    # Order URLs
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
]
