from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from analysis.models import Packet
from analysis.packet.serializers.get.list import PacketListSerializer


class PacketListView(generics.ListAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['branch']

    # def get_queryset(self):
    #     return Packet.objects.filter(analysis__isnull=False).distinct()
