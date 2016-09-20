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


class IOProductStockViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing IOProductStock
    """
    queryset = IOProductStock.objects.all()
    serializer_class = IOProductStockSerializer


class ItemResourceStockViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing ItemResourceStock
    """
    queryset = ItemResourceStock.objects.all()
    serializer_class = ItemResourceStockSerializer


class IOItemResourceStockViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing IOItemResourceStock
    """
    queryset = IOItemResourceStock.objects.all()
    serializer_class = IOItemResourceStockSerializer






