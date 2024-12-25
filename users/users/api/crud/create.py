from rest_framework import generics

from users.models.user import User
from users.users.serializers.crud.crud import UserCrudSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCrudSerializer
