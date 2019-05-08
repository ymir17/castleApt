from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Log_in/login.html')