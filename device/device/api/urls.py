from django.urls import path, include

urlpatterns = [
    path('crud/', include('device.device.api.crud.urls')),
    path('get/', include('device.device.api.get.urls')),
]
