from django.urls import path

from .create import UserRequestCreateView
from .delete import UserRequestDeleteView, UserRequestAnalysisDeleteView
from .update import UserRequestUpdateView

urlpatterns = [
    path('create/', UserRequestCreateView.as_view()),
    path('delete/<int:id>', UserRequestDeleteView.as_view()),
    path('delete_request_analysis/', UserRequestAnalysisDeleteView.as_view()),
    path('update/<int:pk>', UserRequestUpdateView.as_view()),
]
