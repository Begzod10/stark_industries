from django.urls import path

from .list import DeviceList
from .retrieve import DeviceDetail, UsersDeviceAnalysis, UsersAnalysisResultRetrieve

urlpatterns = [
    path('list/', DeviceList.as_view()),
    path('profile/<int:pk>', DeviceDetail.as_view()),
    path('user-analysis/<int:pk>', UsersDeviceAnalysis.as_view()),
    path('analysis-result/<int:pk>', UsersAnalysisResultRetrieve.as_view()),
]
