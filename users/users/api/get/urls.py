from django.urls import path

from users.users.api.get.get import UserTimeTableProfileView
from users.users.api.get.check_username import CheckUsernameAvailability
from users.users.api.get.check_time import DoctorAvailabilityView

urlpatterns = [
    path('time_table_profile/<int:pk>', UserTimeTableProfileView.as_view(), name='time_table_profile'),
    path('check_doctor_time/', DoctorAvailabilityView.as_view(), name='check_doctor_time'),
    path('check_username/', CheckUsernameAvailability.as_view(), name='check_username'),
]
