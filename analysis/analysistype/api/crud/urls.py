from django.urls import path, include

from analysis.analysistype.api.crud.update import AnalysisTypeUpdateView
from analysis.analysistype.api.crud.delete import AnalysisTypeDestroyView
from analysis.analysistype.api.crud.create import AnalysisTypeCreateView

urlpatterns = [
    path('create/', AnalysisTypeCreateView.as_view(), name='create'),
    path('update/<int:pk>/', AnalysisTypeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', AnalysisTypeDestroyView.as_view(), name='delete')
]
