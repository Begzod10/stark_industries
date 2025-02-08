from users.models.user import User
from rest_framework.views import APIView
from rest_framework.response import Response


class CheckUsernameAvailability(APIView):
    def get(self, request, *args, **kwargs):
        username = request.query_params.get("username", "").strip()
        user_id = request.query_params.get("user_id")

        if not username:
            return Response({"available": False, "message": "Username is required"})

        if not user_id:
            is_available = not User.objects.filter(username=username).exists()
            return Response({
                "available": is_available,
                "message": "Username is available" if is_available else "Username is taken"
            })

        existing_user = User.objects.filter(username=username).first()

        if existing_user:
            if str(existing_user.id) == user_id:
                return Response({"available": True, "message": "This is your current username"})

            return Response({"available": False, "message": "Username is taken"})

        return Response({"available": True, "message": "Username is available"})
