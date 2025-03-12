from rest_framework import serializers
from analysis.packet.serializers.get.retrieve import PacketSerializer
from analysis.models import Analysis
from analysis.container.serializers.get.list import ContainerListSerializer
from device.device.serializers.get.retrieve import DeviceRetrieveSerializer


class AnalysisGetSerializer(serializers.ModelSerializer):
    device = serializers.CharField(source='device.name', required=False)
    container = serializers.CharField(source='container.name', required=False)
    type = serializers.SerializerMethodField()
    packet = serializers.CharField(source='packet.name', required=False)

    class Meta:
        model = Analysis
        fields = ['id', 'name', 'device', 'container', 'type', 'packet', 'price', 'code_name']

    def get_type(self, obj):
        return obj.type.name if obj.type else None


# Ensure both ID and Name are included


class AnalysisSerializer(serializers.ModelSerializer):
    packet = PacketSerializer()  # Nest PacketSerializer
    container = ContainerListSerializer()
    device = DeviceRetrieveSerializer()

    class Meta:
        model = Analysis
        fields = ['id', 'name', 'packet', 'price', 'code_name', 'container', 'device']
