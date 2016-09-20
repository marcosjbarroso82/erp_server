from rest_framework import viewsets
from .models import DeliveryGroup, Delivery, Distribution
from .serializers import DeliveryGroupSerializer, DeliverySerializer, DistributionSerializer


class DeliveryGroupViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing DeliveryGroup
    """
    queryset = DeliveryGroup.objects.all()
    serializer_class = DeliveryGroupSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Delivery
    """
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DistributionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Distribution
    """
    queryset = Distribution.objects.all()
    serializer_class = DistributionSerializer

