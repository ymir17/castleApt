from django.shortcuts import render, redirect
from

# Create your views here.

def index(request):
    properties = {'property': }
    return render(request, 'search/search.html')