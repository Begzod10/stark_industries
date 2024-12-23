from django.urls import path

from .crud import BranchCreateView
from .crud import BranchDeleteView
from .crud import BranchUpdateView

urlpatterns = [
    path('create/', BranchCreateView.as_view()),
    path('delete/<int:id>', BranchDeleteView.as_view()),
    path('update/<int:id>', BranchUpdateView.as_view()),
]