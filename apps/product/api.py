import django_filters

from rest_framework import filters
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductFilter(filters.FilterSet):
    stock_lte = django_filters.MethodFilter(action='filter_by_stock_lte', distinct=True)

    def filter_by_stock_lte(self, queryset, value):
        return queryset.filter(stock__quantity__lte=value)

    class Meta:
        model = Product


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter
