from django.urls import path

from .create import PacketCreateView
from .delete import PacketDeleteView
from .update import PacketUpdateView

urlpatterns = [
    path('create/', PacketCreateView.as_view()),
    path('delete/<int:pk>', PacketDeleteView.as_view()),
    path('update/<int:pk>', PacketUpdateView.as_view()),
]
