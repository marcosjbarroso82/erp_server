import django_filters

from rest_framework import filters, status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import Product, ProductVariant, Category, ProductImage
from .serializers import ProductSerializer, ProductVariantSerializer, CategorySerializer, ProductImageSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()

    @detail_route(methods=['get'])
    def default(self, request, *args, **kwargs):
        try:
            self.get_object().set_default()
            return super(ProductImageViewSet, self).retrieve(request, *args, **kwargs)
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class ProductVariantFilter(filters.FilterSet):
    stock_lte = django_filters.MethodFilter(action='filter_by_stock_lte', distinct=True)
    #min_price = django_filters.NumberFilter(name="price", lookup_expr='gte')
    #max_price = django_filters.NumberFilter(name="price", lookup_expr='lte')

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