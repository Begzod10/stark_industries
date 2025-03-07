from django.urls import path

from .crud import JobCreateView, JobDeleteView, JobUpdateView

urlpatterns = [
    path('create/', JobCreateView.as_view()),
    path('delete/<int:pk>', JobDeleteView.as_view()),
    path('update/<int:pk>', JobUpdateView.as_view()),
]
