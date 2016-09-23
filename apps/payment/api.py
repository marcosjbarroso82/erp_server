from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Balances
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_fields = ('order',)
