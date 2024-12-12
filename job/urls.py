from django.urls import path, include

urlpatterns = [

    path('job/', include('job.jobs.api.crud.urls')),
]
