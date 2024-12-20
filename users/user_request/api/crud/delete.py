from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from users.models.user import UserRequest
from users.user_request.serializers.crud.serializers import UserRequestCreateUpdateSerializer


class UserRequestDeleteView(generics.DestroyAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestCreateUpdateSerializer

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({"message": "UserJobs deleted successfully."}, status=status.HTTP_200_OK)
