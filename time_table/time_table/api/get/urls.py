from django.urls import path

from job.job.api.get.list import JobList
from job.job.api.get.retriviev import JobRetrieve

urlpatterns = [
    path('', JobList.as_view(), name='job_list'),
    path('<int:pk>', JobRetrieve.as_view(), name='job_retrieve'),
]
