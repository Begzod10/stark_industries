from django.urls import path, include
from users.patients.api import PatientList

urlpatterns = [
    path('', PatientList.as_view()),

]
