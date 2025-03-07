from django.urls import path, include
from .views import post_data

urlpatterns = [
    path('analysis_type/crud/', include('analysis.analysistype.api.crud.urls')),
    path('analysis_type/get/', include('analysis.analysistype.api.get.urls')),

    path('paket/', include('analysis.packet.api.urls')),

    path('analysis/crud/', include('analysis.analysis.api.crud.urls')),
    path('analysis/get/', include('analysis.analysis.api.get.urls')),

    path('analysis/post/', post_data, name='post_data'),
]
