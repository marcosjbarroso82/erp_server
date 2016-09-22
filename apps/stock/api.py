from rest_framework import viewsets
from .models import ProductStock, IOProductStock, ItemResourceStock, IOItemResourceStock
from .serializers import IOItemResourceStockSerializer, IOProductStockSerializer, ItemResourceStockSerializer, \
    ProductStockSerializer


class ProductStockViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing ProductStock
    """
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer
    filter_fields = ('item',)
    search_fields = ('item__name', 'item__sku')


class IOProductStockViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing IOProductStock
    """
    queryset = IOProductStock.objects.all()
    serializer_class = IOProductStockSerializer
    filter_fields = ('stock',)
    search_fields = ('stock__item__name', 'stock__item__sku')


class ItemResourceStockViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing ItemResourceStock
    """
    queryset = ItemResourceStock.objects.all()
    serializer_class = ItemResourceStockSerializer
    filter_fields = ('item',)
    search_fields = ('item__name', 'item__sku')



class IOItemResourceStockViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing IOItemResourceStock
    """
    queryset = IOItemResourceStock.objects.all()
    serializer_class = IOItemResourceStockSerializer
    filter_fields = ('stock',)
    search_fields = ('stock__item__name', 'stock__item__sku')






