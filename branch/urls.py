from django.urls import path, include

urlpatterns = [
    path('location/', include('branch.locations.api.crud.urls')),
    path('branch/', include('branch.branches.api.crud.urls')),
]
