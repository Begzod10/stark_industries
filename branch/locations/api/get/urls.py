from django.urls import path

from .list import LocationList

urlpatterns = [
    path('', LocationList.as_view()),
]
