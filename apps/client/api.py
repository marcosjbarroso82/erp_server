from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Balances
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    search_fields = ('first_name',)
