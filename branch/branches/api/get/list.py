from rest_framework.generics import ListAPIView
from branch.models import Branch
from branch.branches.serializers.get.retrieve import BranchRetrieveSerializer


class BranchListView(ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchRetrieveSerializer
