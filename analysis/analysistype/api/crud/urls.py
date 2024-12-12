from django.urls import path, include

from analysis.analysistype.api.crud.update import AnalysisTypeUpdateView
from analysis.analysistype.api.crud.delete import AnalysisTypeDestroyView

urlpatterns = [
    path('update/<int:pk>', AnalysisTypeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AnalysisTypeDestroyView.as_view(), name='delete')
]
