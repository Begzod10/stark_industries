from rest_framework import viewsets

from users.models import User
from users.patients.serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = User.objects.filter(User.job__name != '').all()

    def get_queryset(self):
        queryset = User.objects.filter(User.job__name != '', User.branch == 1).all()
        return queryset
