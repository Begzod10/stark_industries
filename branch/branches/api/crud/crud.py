from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from branch.models import Branch
from branch.branches.serializers.crud.crud import BranchSerializer


class BranchCreateView(generics.CreateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()


class BranchUpdateView(generics.UpdateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()


class BranchDeleteView(generics.DestroyAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
