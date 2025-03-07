from django.urls import path
from job.jobs.api.get.get_job import JobListView, GetDoctorsList, UserRequestView, JobRetrieveView

urlpatterns = [
    path('job_list/', JobListView.as_view()),
    path('<int:pk>', JobRetrieveView.as_view(), name='job_retrieve'),
    path('doctor_list/', GetDoctorsList.as_view()),
    path('doctor_clients/', UserRequestView.as_view()),

]
