from rest_framework import generics

from analysis.container.serializers.get.list import ContainerListSerializer
from analysis.models import Container


class ContainerList(generics.ListAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerListSerializer