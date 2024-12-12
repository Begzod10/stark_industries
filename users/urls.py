from django.urls import path, include

urlpatterns = [
    path('users/crud', include('users.users.api.crud.urls')),
]
