from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer

from branch.models import Branch


class BranchRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
