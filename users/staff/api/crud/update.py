from rest_framework import generics

from users.models import User
from users.staff.serializers.crud.serializers import StaffSerializer, StaffSerializerPassword


class StaffUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = StaffSerializer


class StaffUpdatePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = StaffSerializerPassword
