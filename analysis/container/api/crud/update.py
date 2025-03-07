from rest_framework import generics

from analysis.container.serializers.crud.crud import ContainerCrudSerializer
from analysis.models import Container


class ContainerUpdateView(generics.UpdateAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerCrudSerializer