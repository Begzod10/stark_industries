from rest_framework import generics
from rest_framework.exceptions import NotFound

from analysis.models import Analysis
from device.device.serializers.get.retrieve import DeviceRetrieveSerializer, UsersDeviceAnalysisSerializer, \
    UserAnalysisResultSerializer
from device.models import Device
from users.models.analysis import UserAnalysis


class DeviceDetail(generics.RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceRetrieveSerializer


class UsersDeviceAnalysis(generics.ListAPIView):
    queryset = UserAnalysis.objects.all()
    serializer_class = UsersDeviceAnalysisSerializer

    def get_queryset(self):
        if 'pk' not in self.kwargs or getattr(self, 'swagger_fake_view', False):
            return Analysis.objects.none()
        try:
            analysis = Analysis.objects.filter(device_id=self.kwargs['pk']).all()
            queryset = UserAnalysis.objects.filter(analysis__in=analysis).distinct()

        except UserAnalysis.DoesNotExist:
            raise NotFound()
        return queryset


class UsersAnalysisResultRetrieve(generics.RetrieveAPIView):
    queryset = UserAnalysis.objects.all()
    serializer_class = UserAnalysisResultSerializer

    def get_queryset(self):
        if 'pk' not in self.kwargs or getattr(self, 'swagger_fake_view', False):
            return UserAnalysis.objects.none()
        try:
            return UserAnalysis.objects.filter(id=self.kwargs['pk'])
        except UserAnalysis.DoesNotExist:
            raise NotFound()
