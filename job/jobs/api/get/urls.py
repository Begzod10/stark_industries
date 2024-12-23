from django.urls import path
from job.jobs.api.get.get_job import JobListView

urlpatterns = [
    path('job_list/', JobListView.as_view()),
]
