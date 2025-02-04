from rest_framework import generics, filters

from users.models import User
from users.patients.serializers import PatientSerializer

from django_filters.rest_framework import DjangoFilterBackend


class PatientList(generics.ListAPIView):
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email']
    filterset_fields = ['branch']  # Enables filtering by branch

    def get_queryset(self):
        return User.objects.filter(userjobs__job__name__isnull=False).distinct()
