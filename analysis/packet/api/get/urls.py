from django.urls import path

from analysis.packet.api.get.list import PacketListView
from analysis.packet.api.get.retreive import PacketRetreiveView

urlpatterns = [
    path('list/', PacketListView.as_view()),
    path('<int:pk>/', PacketRetreiveView.as_view()),
]
