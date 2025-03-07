from django.urls import path, include

urlpatterns = [
    path('crud/', include('users.user_request.api.crud.urls')),
]

