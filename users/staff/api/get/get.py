from rest_framework import generics

from users.models import User
from users.staff.serializers.get.serializers import StaffSerializerGet
from django.db.models import Q


class StaffListView(generics.ListAPIView):
    from django.db.models import Q

    queryset = User.objects.filter(deleted=False) \
        .filter(~Q(userjobs__job__name="admin")) \
        .filter(~Q(userjobs__job__name="patient"))  # Exclude users with 'patient' job

    serializer_class = StaffSerializerGet


class StaffListDeletedView(generics.ListAPIView):
    queryset = User.objects.filter(deleted=True).all()
    serializer_class = StaffSerializerGet


class StaffDetailView(generics.RetrieveAPIView):
    queryset = User.objects.filter(deleted=False).all()
    serializer_class = StaffSerializerGet
