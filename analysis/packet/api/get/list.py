from rest_framework import generics

from analysis.models import Packet
from analysis.packet.serializers.get.list import PacketListSerializer


class PacketListView(generics.ListAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketListSerializer
