from rest_framework import serializers
from .models import DeliveryGroup, Delivery, Distribution, DELIVERY_STATUS_OPTIONS
from apps.order.serializers import OrderItemSerializer


class DistributionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distribution
        fields = '__all__'



class DeliveryGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryGroup
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    #item = OrderItemSerializer(read_only=True)

    class Meta:
        model = Delivery
        fields = '__all__'



