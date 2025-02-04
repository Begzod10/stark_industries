from rest_framework import serializers

from branch.models import Location


class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
