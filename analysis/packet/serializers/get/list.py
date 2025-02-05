from rest_framework import serializers

from analysis.models import Packet
from analysis.analysis.serializers.get.get import AnalysisGetSerializer


class PacketListSerializer(serializers.ModelSerializer):
    analysis = AnalysisGetSerializer(many=True, read_only=True, source='analysis_set')
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Packet
        fields = ['id', 'name', 'analysis', 'total_price', 'branch']

    def get_total_price(self, obj):
        return sum(analysis.price for analysis in obj.analysis_set.all())
