from rest_framework import generics

from analysis.container.serializers.crud.crud import ContainerCrudSerializer
from analysis.models import Container


class ContainerCreateView(generics.CreateAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerCrudSerializer
