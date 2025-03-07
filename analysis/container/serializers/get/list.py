from analysis.models import Container
from rest_framework import serializers

class ContainerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'