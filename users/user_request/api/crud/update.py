from rest_framework import generics

from users.models.user import UserRequest
from users.user_request.serializers.crud.serializers import UserRequestCreateUpdateSerializer


class UserRequestUpdateView(generics.UpdateAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestCreateUpdateSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # partial=True ni to'g'ri qo'shish
        return super().update(request, *args, **kwargs)
