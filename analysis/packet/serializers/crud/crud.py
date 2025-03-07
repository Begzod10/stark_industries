from rest_framework import serializers

from analysis.models import Packet


class PacketCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packet
        fields = '__all__'
