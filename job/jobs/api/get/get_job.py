from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from job.models import Job
from job.jobs.serializers.crud.crud import JobSerializer, DoctorSerializer
from users.models.user import User, UserRequest
from django.utils.timezone import now
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta, datetime
from users.user_request.serializers.get.get import UserRequestSerializer

from job.jobs.filters.doctor_filter import UserFilter


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobRetrieveView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class GetDoctorsList(generics.ListAPIView):
    queryset = User.objects.filter(userjobs__job__has_client=True).all()
    serializer_class = DoctorSerializer


class UserRequestView(APIView):
    def get(self, request, *args, **kwargs):
        doctor_id = request.query_params.get('doctor_id')
        request_type = request.query_params.get('type')
        date_str = request.query_params.get('date')

        if not doctor_id or not request_type or not date_str:
            return Response({"error": "doctor_id, type va date talab qilinadi"}, status=400)

        try:
            doctor_id = int(doctor_id)
            selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return Response({"error": "Noto'g'ri formatdagi ID yoki sana"}, status=400)

        filters = Q(doctor_id=doctor_id) & Q(date__isnull=False)

        if request_type == "day":
            filters &= Q(date=selected_date)
        elif request_type == "week":
            start_of_week = selected_date - timedelta(days=selected_date.weekday())
            end_of_week = start_of_week + timedelta(days=6)
            filters &= Q(date__range=[start_of_week, end_of_week])
        elif request_type == "month":
            filters &= Q(date__year=selected_date.year, date__month=selected_date.month)
        else:
            return Response({"error": "Noto'g'ri type (faqat 'day', 'week', 'month')"}, status=400)

        user_requests = UserRequest.objects.filter(filters)
        serializer = UserRequestSerializer(user_requests, many=True)

        return Response(serializer.data, status=200)
