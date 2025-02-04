from django.urls import path

from users.patients.api import PatientList, PatientListView
from users.patients.delete import PatientDelete

urlpatterns = [
    path('', PatientList.as_view()),
    path('list/', PatientListView.as_view()),
    path('delete/<int:pk>/', PatientDelete.as_view()),
]
