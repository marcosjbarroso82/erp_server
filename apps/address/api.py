from rest_framework import viewsets
from .models import Address
from .serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Balances
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
