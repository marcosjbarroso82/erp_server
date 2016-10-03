import django_filters

from rest_framework import filters
from rest_framework import viewsets

from .models import Product, ProductVariant, Category, ProductImage
from .serializers import ProductSerializer, ProductVariantSerializer, CategorySerializer, CustomProductImageSerializer


class CustomProductImageViewSet(viewsets.ModelViewSet):
    serializer_class = CustomProductImageSerializer
    queryset = ProductImage.objects.all()



class ProductVariantFilter(filters.FilterSet):
    stock_lte = django_filters.MethodFilter(action='filter_by_stock_lte', distinct=True)

    def filter_by_stock_lte(self, queryset, value):
        return queryset.filter(stock__quantity__lte=value)

    class Meta:
        model = ProductVariant


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ('name',)


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ('name', 'category__name', 'variants__name')
    filter_fields = ('category', )


class ProductVariantViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Products variants
    """
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    filter_class = ProductVariantFilter
    search_fields = ('name', 'sku')
    filter_fields = ('stock_lte', 'product', 'product__category')