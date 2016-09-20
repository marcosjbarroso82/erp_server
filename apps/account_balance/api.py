from rest_framework import viewsets
from .models import Balance
from .serializers import BalanceSerializer


class BalanceViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Balances
    """
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
