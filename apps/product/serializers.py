from rest_framework import serializers
from .models import Product, ProductImage, ProductVariant, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('slug', )


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        exclude = ('deleted', )
        read_only_fields = ('default', )


class ProductVariantSerializer(serializers.ModelSerializer):
    stock_quantity = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    #variantions = ProductVariantSerializer(many=True)
    images = ProductImageSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
