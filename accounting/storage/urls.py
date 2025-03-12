from django.urls import path
from .views import StorageListCreateView, StorageRetrieveUpdateDestroyView

urlpatterns = [
    path('storages/', StorageListCreateView.as_view(), name='storage-list-create'),
    path('storages/<int:pk>/', StorageRetrieveUpdateDestroyView.as_view(), name='storage-detail'),
]
