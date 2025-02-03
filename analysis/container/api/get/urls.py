from django.urls import path

from .list import ContainerList
from .retrieve import ContainerRetrieveView

urlpatterns = [
    path('<int:pk>/', ContainerRetrieveView.as_view(), name='container-retrieve'),
    path('', ContainerList.as_view(), name='container-list'),
]
