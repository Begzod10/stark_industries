from django.urls import path,include
urlpatterns = [
    path('get/', include('job.jobs.api.get.urls')),
]