from rest_framework import serializers
from .models import ItemResource


class ItemResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemResource
        fields = '__all__'
