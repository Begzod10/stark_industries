from django.urls import path, include

urlpatterns = [
    path('crud/', include('analysis.container.api.crud.urls')),
    path('get/', include('analysis.container.api.get.urls')),
]