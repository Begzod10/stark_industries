from django.urls import path, include

urlpatterns = [
    path('location/', include('branch.locations.api.crud.urls')),
    path('location/get/', include('branch.locations.api.get.urls')),
    path('branch/', include('branch.branches.api.crud.urls')),
    path('branch_get/', include('branch.branches.api.get.urls')),
]
