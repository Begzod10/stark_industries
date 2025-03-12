from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from analysis.laboratory.serializers.lab import LaboratoryAnalysisSerializer
from users.models import UserAnalysis
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


class LaboratoryAnalysisView(ListAPIView):
    serializer_class = LaboratoryAnalysisSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    queryset = UserAnalysis.objects.all()
    filterset_fields = ['branch']


