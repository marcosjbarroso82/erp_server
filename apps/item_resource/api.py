from rest_framework import viewsets
from .models import ItemResource
from .serializers import ItemResourceSerializer


class ItemResourceViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Balances
    """
    queryset = ItemResource.objects.all()
    serializer_class = ItemResourceSerializer
