from rest_framework import generics
from accounting.models import Storage
from .serializers import StorageSerializer


class StorageListCreateView(generics.ListCreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class StorageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
