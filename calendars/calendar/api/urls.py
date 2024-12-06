from django.urls import path,include

urlpatterns = [
    path('crud/', include('calendars.calendar.api.crud.urls')),
]