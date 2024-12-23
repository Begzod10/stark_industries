from rest_framework import generics

from users.models import User
from users.staff.serializers.crud.serializers import StaffSerializer


class StaffDestroyView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = StaffSerializer
