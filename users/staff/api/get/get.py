from rest_framework import generics

from users.models import User
from users.staff.serializers.get.serializers import StaffSerializerGet


class StaffListView(generics.ListAPIView):
    queryset = User.objects.filter(deleted=False).all()
    serializer_class = StaffSerializerGet


class StaffListDeletedView(generics.ListAPIView):
    queryset = User.objects.filter(deleted=True).all()
    serializer_class = StaffSerializerGet


class StaffDetailView(generics.RetrieveAPIView):
    queryset = User.objects.filter(deleted=False).all()
    serializer_class = StaffSerializerGet
