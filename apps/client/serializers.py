from rest_framework import serializers
from .models import Client
from apps.address.serializers import AddressSerializer
from apps.address.models import Address
from django.db import transaction


class ClientAddressSerializer(AddressSerializer):
    class Meta:
        model = Address
        fields = ['street']


class ClientSerializer(serializers.ModelSerializer):
    address = ClientAddressSerializer()

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('balance',)

    def create(self, validated_data):
        with transaction.atomic():
            address = Address(**validated_data.pop('address'))
            address.save()
            client = Client.objects.create(address=address, **validated_data)
            return client

    def update(self, instance, validated_data):
        if validated_data.get('address'):
            address = validated_data.pop('address')
            instance.address.street = address['street']
            instance.address.save()

        if validated_data.get('first_name'):
            instance.first_name = validated_data.get('first_name')

        instance.save()
        return instance

