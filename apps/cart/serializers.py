from rest_framework import serializers
from apps.product.models import Product as ProductVariant
from apps.product.serializers import ProductSerializer as ProductVariantSerializer


class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""
    def to_internal_value(self, data):
        return data
    def to_representation(self, value):
        return value


class NewCartItemSerializer(serializers.Serializer):
    variant = ProductVariantSerializer()
    product = serializers.IntegerField()
    quantity = serializers.IntegerField()
    price = serializers.FloatField()
    msg = serializers.CharField()
    data = JSONSerializerField()
    sub_total = serializers.FloatField(read_only=True)
    sku = serializers.SerializerMethodField()

    def get_sku(self, obj):
        variant = ProductVariant.objects.get(id=obj.product)
        return variant.sku


class NewCartSerializer(serializers.Serializer):
    created_date = serializers.DateTimeField()
    updated_date = serializers.DateTimeField()
    items = NewCartItemSerializer(many=True)
    total = serializers.FloatField(read_only=True)

