from rest_framework import generics

from analysis.container.serializers.crud.crud import ContainerCrudSerializer
from analysis.models import Container
from rest_framework.response import Response
from rest_framework import status

class ContainerDestroyView(generics.DestroyAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerCrudSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Container deleted successfully."}, status=status.HTTP_200_OK)