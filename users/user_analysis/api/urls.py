from django.urls import path, include

urlpatterns = [
    path('crud/', include('users.user_job.api.crud.urls')),
    path('get/', include('users.user_analysis.api.get.urls')),
    path('crud/', include('users.user_analysis.api.crud.urls')),
]
