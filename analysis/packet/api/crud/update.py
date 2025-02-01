from rest_framework import generics

from analysis.models import Packet
from analysis.packet.serializers.crud.crud import PacketCrudSerializer


class PacketUpdateView(generics.UpdateAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketCrudSerializer
