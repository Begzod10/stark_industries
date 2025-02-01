from rest_framework import generics

from analysis.models import Packet
from analysis.packet.serializers.crud.crud import PacketCrudSerializer


class PacketCreateView(generics.CreateAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketCrudSerializer
