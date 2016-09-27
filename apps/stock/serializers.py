from rest_framework import serializers
from .models import ProductStock, IOProductStock, ItemResourceStock, IOItemResourceStock


class ProductStockSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    reserved_stock = serializers.FloatField(read_only=True)

    def get_product_name(self, obj):
        return obj.item.name

    class Meta:
        model = ProductStock
        fields = '__all__'


class IOProductStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = IOProductStock
        fields = '__all__'


class ItemResourceStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemResourceStock
        fields = '__all__'


class IOItemResourceStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = IOItemResourceStock
        fields = '__all__'


