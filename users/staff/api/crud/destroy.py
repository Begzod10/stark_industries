from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from users.staff.serializers.crud.serializers import StaffSerializer


class StaffDestroyView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = StaffSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
