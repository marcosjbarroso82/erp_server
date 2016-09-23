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


    # def create(self, request):
    #     # import ipdb; ipdb.set_trace()
    #     items_data = request.date.pop('items')
    #
    #     cart = NewCart(created_date=request.data.get('created_date'))
    #     items = request.data.get('items')
    #
    #     if items:
    #         for item in items:
    #             try:
    #                 cart_item = cart.add_item(item.get('product'), item.get('quantity', 0), item.get('data', {}))
    #             except Exception as e:
    #                 raise
    #                 pass
    #
    #
    #     serializer = NewCartSerializer(cart, many=False)
    #     response = serializer.data
    #     # response['request'] = request.data
    #     # response['orig_items'] = it