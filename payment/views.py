from django.shortcuts import render, get_object_or_404
from property.models import Properties, PropImages

# Create your views here.

def index(request, id):
    return render(request, 'Payment/payment.html', {
        'property': get_object_or_404(Properties, pk=id),
        'images': PropImages.objects.filter(propImgUrl__contains='_00').order_by("propertyId_id")
    })
