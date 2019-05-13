from django.shortcuts import render
from property.models import Properties, PropImages




# Create your views here.
def index(request):
    return render(request, 'Property/property.html')