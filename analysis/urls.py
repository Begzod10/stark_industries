from django.urls import path, include
from .views import post_data


urlpatterns = [
    path('analysis_type/crud/', include('analysis.analysistype.api.crud.urls')),
    path('analysis/crud/', include('analysis.analysis.api.crud.urls')),
    path('analysis/post/', post_data, name='post_data'),
]
