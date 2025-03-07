from rest_framework.generics import ListAPIView
from branch.models import Branch
from django_filters.rest_framework import DjangoFilterBackend
from branch.branches.serializers.get.retrieve import BranchRetrieveSerializer


class BranchListView(ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchRetrieveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location']
