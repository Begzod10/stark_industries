from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from users.models.analysis import UserAnalysis
from users.user_analysis.serializers.get.retrieve import UserAnalysisGetSerializer
import pprint

from rest_framework.response import Response
from collections import defaultdict


class UsersAnalysisList(ListAPIView):
    queryset = UserAnalysis.objects.all()
    serializer_class = UserAnalysisGetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        packet_data = defaultdict(lambda: {"packet_id": None, "packet_name": None, "analysis_list": []})
        analysis_list = []

        for item in serializer.data:
            analysis = item.get("analysis")
            if analysis:
                packet = analysis.get("packet")
                if isinstance(packet, dict):  # Ensure packet is a dictionary
                    packet_id = packet.get("id")
                    packet_name = packet.get("name")

                    if packet_id:
                        packet_data[packet_id]["packet_id"] = packet_id
                        packet_data[packet_id]["packet_name"] = packet_name
                        packet_data[packet_id]["analysis_list"].append(item)
                else:
                    analysis_list.append(item)
            else:
                analysis_list.append(item)

        return Response({
            "info": {
                "packet": list(packet_data.values()),
                "analysis_list": analysis_list
            }
        })
