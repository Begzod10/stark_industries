from django.urls import path
from job.jobs.api.get.get_job import JobListView, JobRetrieveView

urlpatterns = [
    path('job_list/', JobListView.as_view()),
    path('<int:pk>', JobRetrieveView.as_view(), name='job_retrieve'),
]
