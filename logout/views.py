from django.contrib.auth import logout
from django.shortcuts import render


def index(request):
    logout(request)
    return render(request, 'home/home.html')
