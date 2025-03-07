from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from users.models.user import User
from .serializers import PatientListSerializer


class PatientDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = PatientListSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response({'message', "Patient deleted successfully"}, status=status.HTTP_200_OK)
