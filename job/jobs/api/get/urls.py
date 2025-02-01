from django.urls import path
from job.jobs.api.get.get_job import JobListView, GetDoctorsList

urlpatterns = [
    path('job_list/', JobListView.as_view()),
    path('doctor_list/', GetDoctorsList.as_view()),
]
