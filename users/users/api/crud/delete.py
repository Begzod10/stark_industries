from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models.user import User

from users.users.serializers.crud.crud import UserCrudSerializer


class UserDestroyView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserCrudSerializer
