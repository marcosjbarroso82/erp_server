from rest_framework import serializers
from .models import Product, ProductImage, ProductVariant, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductVariantSerializer(serializers.ModelSerializer):
    #reserved_stock = serializers.FloatField(read_only=True)
    #available_stock = serializers.FloatField(read_only=True)
    stock_quantity = serializers.FloatField(read_only=True)

    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    #variantions = ProductVariantSerializer(many=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
