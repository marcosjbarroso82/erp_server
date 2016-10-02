from rest_framework import serializers
from .models import OrderItem, Order, ORDER_STATUS_OPTIONS
from django.db import transaction

from apps.core.serializers import BaseModelSerializer


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ('order',)


class OrderSerializer(BaseModelSerializer):
    #items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('delivered', 'payed', 'total')
        fields_config = {
            'update': {
                'fields': ('status',)
            },
            'partial_update': {
                'fields': ('status',)
            }
        }

    def update(self, instance, validated_data):
        # Exclude items from serializer.
        validated_data.pop('items')
        return super().update(instance, validated_data)

    def create(self, validated_data):
        with transaction.atomic():
            items_data = validated_data.pop('items')
            order = Order.objects.create(**validated_data)
            for item_data in items_data:
                # OrderItem.objects.create(order=order, **item_data)
                order.add_item(**item_data)
            return order
