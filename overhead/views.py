from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Overhead, OverheadType
from .serializers import OverheadSerializer, OverheadTypeSerializer


class OverheadTypeViewSet(viewsets.ModelViewSet):
    queryset = OverheadType.objects.all()
    serializer_class = OverheadTypeSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['order', 'name']


class OverheadViewSet(viewsets.ModelViewSet):
    queryset = Overhead.objects.filter(deleted=False)
    serializer_class = OverheadSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'payment', 'branch', 'type', 'created']
    ordering_fields = ['created', 'price']

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
