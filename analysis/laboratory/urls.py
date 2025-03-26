from django.urls import path, include
from .views.lab import LaboratoryAnalysisView, LaboratoryUpdateView

urlpatterns = [

    path('list/', LaboratoryAnalysisView.as_view(), name='list'),
    path('update/<pk>/', LaboratoryUpdateView.as_view(), name='update'),

]
