from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from calendars.calendar.serializers.crud.serializers import CalendarSerializer
from calendars.models import Calendar


class CalendarDeleteView(generics.DestroyAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({"message": "Calendar deleted successfully."}, status=status.HTTP_200_OK)
