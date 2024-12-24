from django.urls import path, include

from analysis.analysis.api.crud.update import AnalysisUpdateView
from analysis.analysis.api.crud.delete import AnalysisDestroyView
from analysis.analysis.api.crud.create import AnalysisCreateView

urlpatterns = [
    path('create/', AnalysisCreateView.as_view(), name='create'),
    path('update/<int:pk>/', AnalysisUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', AnalysisDestroyView.as_view(), name='delete')
]
