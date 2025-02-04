from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from users.models import User
from users.patients.serializers import PatientSerializer, PatientListSerializer


class PatientList(generics.ListAPIView):
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email']
    filterset_fields = ['branch']

    def get_queryset(self):
        return User.objects.filter(userjobs__job__name="patient", deleted=False).distinct()


class PatientListView(generics.ListAPIView):
    serializer_class = PatientListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email']
    filterset_fields = ['branch']

    def get_queryset(self):
        return User.objects.filter(userjobs__job__name="patient", deleted=False).distinct()
