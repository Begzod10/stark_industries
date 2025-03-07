from django.urls import path

from .crud import LocationCreateView, LocationDeleteView, LocationUpdateView

urlpatterns = [
    path('create/', LocationCreateView.as_view()),
    path('delete/<int:id>', LocationDeleteView.as_view()),
    path('update/<int:id>', LocationUpdateView.as_view()),
]
