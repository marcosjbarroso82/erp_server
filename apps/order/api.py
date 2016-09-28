from rest_framework import viewsets
from .models import Order, OrderItem
from .serializers import OrderItemSerializer, OrderSerializer

from apps.product.models import Product


class OrderViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Order
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_fields = ('_status', 'client')


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing OrderItem
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_fields = ('order',)
    search_fields = ('product_name', 'product__sku')







