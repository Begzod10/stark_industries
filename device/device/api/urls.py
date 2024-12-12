from django.urls import path, include

urlpatterns = [
    path('crud/', include('device.device.api.crud.urls')),
]
