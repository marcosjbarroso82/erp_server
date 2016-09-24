import django_filters

from rest_framework import filters
from rest_framework import viewsets

from .models import ItemResource
from .serializers import ItemResourceSerializer


class ItemResourceFilter(filters.FilterSet):
    stock_lte = django_filters.MethodFilter(action='filter_by_stock_lte', distinct=True)

    def filter_by_stock_lte(self, queryset, value):
        return queryset.filter(stock__quantity__lte=value)

    class Meta:
        model = ItemResource


class ItemResourceViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Balances
    """
    queryset = ItemResource.objects.all()
    serializer_class = ItemResourceSerializer
    filter_class = ItemResourceFilter
