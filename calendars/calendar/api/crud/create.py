from rest_framework import generics

from calendars.calendar.serializers.crud.serializers import CalendarSerializer
from calendars.models import Calendar


class CalendarCreateView(generics.CreateAPIView):
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()
