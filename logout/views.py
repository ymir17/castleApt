from django.shortcuts import render


def index(request):
    return render(request, 'Log_in/login.html')
