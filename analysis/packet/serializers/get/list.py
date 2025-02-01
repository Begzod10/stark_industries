from rest_framework import serializers

from analysis.models import Packet
from analysis.analysis.serializers.get.get import AnalysisGetSerializer


class PacketListSerializer(serializers.ModelSerializer):
    analysis = AnalysisGetSerializer(many=True, read_only=True, source='analysis_set')

    class Meta:
        model = Packet
        fields = ['id', 'name', 'analysis']
