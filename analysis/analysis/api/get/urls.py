from django.urls import path, include

from analysis.analysis.api.get.list import AnalysisListView

urlpatterns = [
    path('list/', AnalysisListView.as_view(), name='list'),
]
