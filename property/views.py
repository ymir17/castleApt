from django.shortcuts import render, get_object_or_404
from property.models import Properties, PropImages




# Create your views here.
def index(request):
    return render(request, 'Property/property.html', {
        'property': get_object_or_404(Properties, pk=propertyId)
    })