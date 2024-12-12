from django.urls import path

from .create import CalendarCreateView
from .delete import CalendarDeleteView
from .update import CalendarUpdateView

urlpatterns = [
    path('create/', CalendarCreateView.as_view()),
    path('delete/<int:id>', CalendarDeleteView.as_view()),
    path('update/<int:id>', CalendarUpdateView.as_view()),
]
