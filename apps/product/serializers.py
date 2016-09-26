from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    reserved_stock = serializers.FloatField(read_only=True)
    available_stock = serializers.FloatField(read_only=True)
    stock_quantity = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
