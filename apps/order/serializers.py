from rest_framework import serializers
from .models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ('order',)


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, required=False)
    payment_status = serializers.IntegerField(read_only=True)
    _status = serializers.IntegerField(read_only=True)
    status = serializers.IntegerField()

    class Meta:
        model = Order
        fields = '__all__'
        # read_only = ['payment_status']

    def update(self, instance, validated_data):
        # Exclude items from serializer.
        validated_data.pop('items')
        return super().update(instance, validated_data)

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            # OrderItem.objects.create(order=order, **item_data)
            order.add_item(**item_data)
        return order
