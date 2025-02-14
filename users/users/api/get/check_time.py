from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import make_aware
from users.models.user import UserRequest, User
from django.db.models import Q, F


class DoctorAvailabilityView(APIView):
    def get(self, request):
        doctor_id = request.query_params.get('doctor_id')
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        user_request_id = request.query_params.get('user_request_id')
        date = request.query_params.get('date')

        doctor = User.objects.get(id=doctor_id)
        from_time = datetime.strptime(from_date, "%H:%M").time()
        to_time = datetime.strptime(to_date, "%H:%M").time()
        check_date = datetime.strptime(date, "%Y-%m-%d").date()

        conflicting_request = UserRequest.objects.filter(
            doctor=doctor,
            date=check_date
        ).filter(
            Q(from_date__lte=to_time) & Q(to_date__gte=from_time)
        ).select_related('patient').first()

        if conflicting_request:

            if user_request_id and conflicting_request.id == int(user_request_id):
                if to_time > conflicting_request.to_date:
                    filter_conflict = UserRequest.objects.filter(
                        doctor=doctor,
                        date=check_date,
                        from_date__lte=to_time,
                        to_date__gte=to_time
                    ).order_by('from_date').first()

                    if filter_conflict:
                        return Response({
                            "available": False,
                            "start": filter_conflict.from_date.strftime("%H:%M"),
                            "end": filter_conflict.to_date.strftime("%H:%M")
                        }, status=status.HTTP_200_OK)
                    else:
                        if from_time >= conflicting_request.from_date and to_time > conflicting_request.to_date:
                            filter_conflict2 = UserRequest.objects.filter(
                                doctor=doctor,
                                date=check_date,
                                from_date__gte=conflicting_request.to_date
                            ).order_by('from_date').first()
                            return Response({
                                "available": False,
                                "start": filter_conflict2.from_date.strftime("%H:%M"),
                                "end": filter_conflict2.to_date.strftime("%H:%M")
                            }, status=status.HTTP_200_OK)
                return Response({"available": True}, status=status.HTTP_200_OK)

            return Response({
                "available": False,
                "start": conflicting_request.from_date.strftime("%H:%M"),
                "end": conflicting_request.to_date.strftime("%H:%M")
            }, status=status.HTTP_200_OK)

        return Response({"available": True}, status=status.HTTP_200_OK)
