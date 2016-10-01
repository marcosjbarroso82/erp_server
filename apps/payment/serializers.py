from rest_framework import serializers
from .models import Payment, PAYMENT_STATUS_CHOICES


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
