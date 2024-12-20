from django.urls import path

from .create import UserRequestCreateView
from .delete import UserRequestDeleteView
from .update import UserRequestUpdateView

urlpatterns = [
    path('create/', UserRequestCreateView.as_view()),
    path('delete/<int:id>', UserRequestDeleteView.as_view()),
    path('update/<int:id>', UserRequestUpdateView.as_view()),
]
