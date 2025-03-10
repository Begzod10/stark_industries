import pprint

from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UsernameCheck(APIView):
    def post(self, request, *args, **kwargs):
        pprint.pprint(request.data)
        username = request.data.get("username", None)
        if username and User.objects.filter(username=username).exists():
            return Response({"message": "Username already exists.", "status": True},
                            status=status.HTTP_200_OK)
        return Response({"message": "Username is available.", "status": False},
                        status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        User.objects.filter(pk=request.user.pk).update(username=request.data['username'])
        return Response({"message": "Username updated successfully."}, status=status.HTTP_200_OK)


# Create your views here.


class UsernameCheckAuthorized(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        pk = request.data.get("pk", None)

        if username is None:
            return Response({"message": "Username is required.", "status": True},
                            status=status.HTTP_200_OK)

        # Filter by username and exclude the user with the given primary key (pk)
        if User.objects.filter(username=username).exclude(pk=pk).exists():
            return Response({"message": "Username already exists.", "status": True},
                            status=status.HTTP_200_OK)

        return Response({"message": "Username is available.", "status": False},
                        status=status.HTTP_200_OK)

