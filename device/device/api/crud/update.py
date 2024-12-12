from rest_framework import generics

from device.device.serializers.crud.serializers import DeviceSerializer
from device.models import Device


class UpdateDevice(generics.UpdateAPIView):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
