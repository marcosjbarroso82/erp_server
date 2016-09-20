from rest_framework import serializers
from .models import DeliveryGroup, Delivery, Distribution


class DistributionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distribution
        fields = '__all__'


class DeliveryGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryGroup
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = '__all__'



