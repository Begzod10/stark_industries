from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from branch.locations.serializers.crud.crud import LocationSerializer
from branch.models import Location


class LocationCreateView(generics.CreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationUpdateView(generics.UpdateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationDeleteView(generics.DestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({"message": "Location deleted successfully."}, status=status.HTTP_200_OK)
