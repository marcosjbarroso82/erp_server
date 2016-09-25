from rest_framework import serializers
from .models import Balance, Ticket


class BalanceSerializer(serializers.ModelSerializer):
    total = serializers.FloatField(read_only=True)
    class Meta:
        model = Balance
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'