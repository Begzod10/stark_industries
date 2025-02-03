from rest_framework import serializers

from analysis.models import Analysis


class AnalysisGetSerializer(serializers.ModelSerializer):
    device = serializers.CharField(source='device.name', required=False)
    container = serializers.CharField(source='container.name', required=False)
    type = serializers.CharField(source='analysistype.name', required=False)
    packet = serializers.CharField(source='packet.name', required=False)

    class Meta:
        model = Analysis
        fields = '__all__'
