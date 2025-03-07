from django.urls import path

from .create import DeviceCreateView
from .delete import DeviceDelete
from .update import UpdateDevice

urlpatterns = [
    path('create/', DeviceCreateView.as_view()),
    path('delete/<int:pk>/', DeviceDelete.as_view()),
    path('update/<int:pk>/', UpdateDevice.as_view()),
]
