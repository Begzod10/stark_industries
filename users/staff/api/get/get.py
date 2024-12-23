from rest_framework import generics

from users.models import User
from users.staff.serializers.crud.serializers import StaffSerializer


class StaffListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = StaffSerializer


class StaffDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = StaffSerializer
