from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from analysis.models import Packet
from analysis.packet.serializers.crud.crud import PacketCrudSerializer


class PacketDeleteView(generics.DestroyAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketCrudSerializer

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({"message": "Packet deleted successfully."}, status=status.HTTP_200_OK)
