from rest_framework import generics

from device.device.serializers.crud.serializers import DeviceSerializer


class DeviceCreateView(generics.CreateAPIView):
    queryset = DeviceSerializer.Meta.model.objects.all()
    serializer_class = DeviceSerializer
