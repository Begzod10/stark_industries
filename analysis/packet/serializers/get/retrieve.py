from rest_framework import serializers
from analysis.models import Packet


class PacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packet
        fields = ['id', 'name', 'branch']
