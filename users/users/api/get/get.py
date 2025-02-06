from rest_framework import generics

from users.models.user import User
from users.users.serializers.get.retriviev import UserRetrieveSerializer


class UserTimeTableProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer
