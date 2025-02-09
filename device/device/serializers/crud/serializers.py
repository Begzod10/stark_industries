from rest_framework import serializers

from device.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    img = serializers.CharField(required=False)

    class Meta:
        model = Device
        fields = '__all__'
