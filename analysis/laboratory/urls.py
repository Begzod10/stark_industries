from django.urls import path, include
from .views.lab import LaboratoryAnalysisView

urlpatterns = [

    path('list/', LaboratoryAnalysisView.as_view(), name='list'),

]
