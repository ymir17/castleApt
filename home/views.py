from django.shortcuts import render
from home.models import Property, PropImages



# Create your views here.
def index(request):
    return render(request, 'Home/home.html')