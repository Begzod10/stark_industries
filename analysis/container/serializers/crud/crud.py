from rest_framework import serializers

from analysis.models import Container


class ContainerCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'
