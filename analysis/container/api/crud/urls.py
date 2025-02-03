from django.urls import path

from .create import ContainerCreateView
from .delete import ContainerDestroyView
from .update import ContainerUpdateView

urlpatterns = [
    path('create/', ContainerCreateView.as_view(), name='container-create'),
    path('<int:pk>/update', ContainerUpdateView.as_view(), name='container-update'),
    path('<int:pk>/delete', ContainerDestroyView.as_view(), name='container-delete'),
]
