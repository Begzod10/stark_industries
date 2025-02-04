from rest_framework import generics

from branch.locations.serializers.get.list import LocationListSerializer, Location


class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationListSerializer
