from rest_framework import serializers

from device.models import Device

class DeviceRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'