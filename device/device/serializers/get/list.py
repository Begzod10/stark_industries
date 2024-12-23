from device.models import Device
from rest_framework import serializers


class DeviceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name','img']