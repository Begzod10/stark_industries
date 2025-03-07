from django.urls import path, include

from analysis.analysistype.api.get.list import AnalysisTypeListView

urlpatterns = [
    path('list/', AnalysisTypeListView.as_view(), name='list'),
    # path('profile/<int:pk>', AnalysisTypeUpdateView.as_view(), name='update'),
]
