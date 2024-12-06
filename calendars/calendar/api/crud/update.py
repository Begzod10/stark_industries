from rest_framework import generics

from calendars.calendar.serializers.crud.serializers import CalendarSerializer
from calendars.models import Calendar


class CalendarUpdateView(generics.UpdateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer