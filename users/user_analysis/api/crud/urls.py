from django.urls import path

from .create import UserAnalysisCreateView
from .delete import UserAnalysisDeleteView
from .update import UserAnalysisUpdateView

urlpatterns = [
    path('create/', UserAnalysisCreateView.as_view()),
    path('delete/<int:id>', UserAnalysisDeleteView.as_view()),
    path('update/<int:id>', UserAnalysisUpdateView.as_view()),
]
