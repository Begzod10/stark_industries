from django.urls import path, include

urlpatterns = [
    path('job_crud/', include('job.jobs.api.crud.urls')),
    path('job_get/', include('job.jobs.api.get.urls')),
]
