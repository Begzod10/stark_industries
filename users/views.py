from django.shortcuts import render
from .models import User


def check_username(request):
    exists = User.objects.filter(id=request.POST.get('id'),username=request.POST.get('username')).exists()
    if exists:
        return {'exists': True}
    return {'exists': False}
# Create your views here.
