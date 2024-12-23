from django.urls import path, include

urlpatterns = [
    path('crud/', include('users.user_job.api.crud.urls')),
]
