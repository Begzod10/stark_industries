from rest_framework import serializers

from analysis.models import Packet


class PacketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packet
        fields = '__all__'
