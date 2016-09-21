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


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing OrderItem
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


    def perform_create(self, serializer):
        serializer.save(product_name=serializer.validated_data['product'].name,
                        price=serializer.validated_data['product'].price)
