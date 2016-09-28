from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    stock_quantity = serializers.FloatField(read_only=True)
    reserved_stock_quantity  = serializers.FloatField(read_only=True)
    available_stock_quantity = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
