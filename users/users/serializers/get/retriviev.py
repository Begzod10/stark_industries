from rest_framework import serializers

from users.models import User, UserRequest, UserAnalysis


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRetrieveSerializer(serializers.ModelSerializer):
    user_request = serializers.SerializerMethodField()
    analysis_list = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'name', 'surname', 'birth_date', 'phone_number', 'address', 'sex', 'branch', 'username',
            'email', 'passport_series', 'passport_number', 'user_request', 'analysis_list'
        ]

    def get_user_request(self, obj):
        user_request = UserRequest.objects.filter(patient=obj).first()
        if user_request:
            return {
                "doctor": user_request.doctor.id,
                "from_date": user_request.from_date,
                "to_date": user_request.to_date,
                "date": user_request.date
            }
        return None

    def get_analysis_list(self, obj):
        user_request = UserRequest.objects.filter(patient=obj).first()
        if not user_request:
            return {"packets": [], "individuals": [], "individual_total_price": 0}

        analyses = UserAnalysis.objects.filter(user=obj, request=user_request)
        packet_list = []
        packet_map = {}
        individual_analyses = []
        individual_total_price = 0

        for analysis in analyses:
            packet = analysis.analysis.packet
            analysis_data = {
                "name": analysis.analysis.name,
                "id": analysis.analysis.id,
                "status": analysis.status,
                "expected_result": analysis.expected_result,
                "result": analysis.result,
                "price": analysis.analysis.price
            }

            if packet:
                if packet.id not in packet_map:
                    packet_info = {
                        "id": packet.id,
                        "name": packet.name,
                        "price": 0,
                        "analysis": []
                    }
                    packet_map[packet.id] = packet_info
                    packet_list.append(packet_info)

                packet_map[packet.id]["analysis"].append(analysis_data)
                packet_map[packet.id]["price"] += analysis.analysis.price
            else:
                individual_analyses.append(analysis_data)
                individual_total_price += analysis.analysis.price

        return {
            "packets": packet_list,
            "individuals": individual_analyses,
            "individual_total_price": individual_total_price
        }
