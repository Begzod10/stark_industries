from rest_framework import generics
from rest_framework.filters import SearchFilter

from device.device.serializers.get.list import DeviceListSerializer
from device.models import Device


class DeviceList(generics.ListAPIView):
    queryset = Device.objects.filter(deleted=False).all()
    serializer_class = DeviceListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
