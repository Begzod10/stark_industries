from django.urls import path

from .crud import JobCreateView, JobDeleteView, JobUpdateView

urlpatterns = [
    path('create/', JobCreateView.as_view()),
    path('delete/<int:id>', JobDeleteView.as_view()),
    path('update/<int:id>', JobUpdateView.as_view()),
]
