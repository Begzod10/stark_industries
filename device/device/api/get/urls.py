from django.urls import path

from .list import DeviceList

urlpatterns = [
    path('list/', DeviceList.as_view()),
]
