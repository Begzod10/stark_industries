from django.urls import path, include

urlpatterns = [
    path('crud/', include('analysis.packet.api.crud.urls')),
    path('get/', include('analysis.packet.api.get.urls')),
]
