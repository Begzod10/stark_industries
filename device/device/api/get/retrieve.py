from rest_framework import generics

from analysis.models import Analysis
from device.device.serializers.get.retrieve import DeviceRetrieveSerializer, UsersDeviceAnalysisSerializer,UserAnalysisResultSerializer
from device.models import Device
from users.models.analysis import UserAnalysis


class DeviceDetail(generics.RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceRetrieveSerializer


class UsersDeviceAnalysis(generics.ListAPIView):
    queryset = UserAnalysis.objects.all()
    serializer_class = UsersDeviceAnalysisSerializer

    def get_queryset(self):
        analysis = Analysis.objects.filter(device_id=self.kwargs['pk']).all()
        queryset = UserAnalysis.objects.filter(analysis__in=analysis).distinct()
        return queryset


class UsersAnalysisResultRetrieve(generics.RetrieveAPIView):
    queryset = UserAnalysis.objects.all()
    serializer_class = UserAnalysisResultSerializer

    def get_queryset(self):
        return UserAnalysis.objects.filter(id=self.kwargs['pk'])
