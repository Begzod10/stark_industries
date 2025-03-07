from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from device.device.serializers.crud.serializers import DeviceSerializer
from device.models import Device


class DeviceDelete(generics.DestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted =True
        instance.save()
        return Response({"message": "Device deleted successfully."}, status=status.HTTP_200_OK)
