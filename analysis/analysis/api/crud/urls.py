from django.urls import path, include

from analysis.analysis.api.crud.update import AnalysisUpdateView
from analysis.analysis.api.crud.delete import AnalysisDestroyView

urlpatterns = [
    path('update/<int:pk>', AnalysisUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AnalysisDestroyView.as_view(), name='delete')
]
