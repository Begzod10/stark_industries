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
        request_id = self.context.get('request_id')
        user_request = UserRequest.objects.filter(patient=obj, id=request_id).first()
        if user_request:
            return {
                "id": user_request.id,
                "doctor": user_request.doctor.id,
                "from_date": user_request.from_date,
                "to_date": user_request.to_date,
                "date": user_request.date
            }
        return None

    def get_analysis_list(self, obj):
        request_id = self.context.get('request_id')
        user_request = UserRequest.objects.filter(patient=obj, id=request_id).first()
        if not user_request:
            return {"packets": [], "individuals": [], "individual_total_price": 0}

        user_analysis = UserAnalysis.objects.filter(user=obj, request=user_request).first()
        if not user_analysis:
            return {"packets": [], "individuals": [], "individual_total_price": 0}

        analyses = user_analysis.analysis.all()
        packet_list = []
        packet_map = {}
        individual_analyses = []
        individual_total_price = 0

        for analysis in analyses:
            packet = analysis.packet
            analysis_data = {
                "name": analysis.name,
                "id": analysis.id,
                "price": analysis.price
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
                packet_map[packet.id]["price"] += analysis.price
            else:
                individual_analyses.append(analysis_data)
                individual_total_price += analysis.price

        return {
            "packets": packet_list,
            "individuals": individual_analyses,
            "individual_total_price": individual_total_price
        }
