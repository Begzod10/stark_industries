from rest_framework import generics

from users.models.user import User
from users.users.serializers.get.retriviev import UserRetrieveSerializer


class UserTimeTableProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        request_id = self.request.query_params.get('request_id')
        if request_id:
            context['request_id'] = request_id
        return context
