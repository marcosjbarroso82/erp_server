from rest_framework import viewsets
from .models import Provider
from .serializers import ProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Provider
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    search_fields = ('name',)
