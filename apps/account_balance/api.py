from rest_framework import viewsets
from .models import Balance, Ticket
from .serializers import BalanceSerializer, TicketSerializer


class BalanceViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Balances
    """
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class TicketViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Tickets
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer