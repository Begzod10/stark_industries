from django.urls import path, include

urlpatterns = [
    path('analysis_type/crud/', include('analysis.analysistype.api.crud.urls')),
    path('analysis/crud/', include('analysis.analysis.api.crud.urls')),
]
