from django.urls import path

from .create import UserJobsCreateView
from .delete import UserJobsDelete
from .update import UserJobsUpdate

urlpatterns = [
    path('create/', UserJobsCreateView.as_view()),
    path('delete/<int:id>', UserJobsDelete.as_view()),
    path('update/<int:id>', UserJobsUpdate.as_view()),
]
