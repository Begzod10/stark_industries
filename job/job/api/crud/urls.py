from django.urls import path

from job.job.api.crud.create import JobCreateApiView
from job.job.api.crud.destroy import JobDestroyApiView
from job.job.api.crud.update import JobUpdateApiView

urlpatterns = [
    path('create/', JobCreateApiView.as_view(), name='create'),
    path('update/<pk>/', JobDestroyApiView.as_view(), name='update'),
    path('delete/<pk>/', JobUpdateApiView.as_view(), name='delete'),
]
