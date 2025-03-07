from rest_framework import generics

from users.models.user import UserRequest
from users.user_request.serializers.crud.serializers import UserRequestCreateUpdateSerializer


class UserRequestCreateView(generics.CreateAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestCreateUpdateSerializer
