from django.shortcuts import render, redirect
from property.models import Properties, PropImages

SORT_BY = (
    'Price Low',
    'Price High',
    'Name',
    'Zip Code'
)

def index(request):
    properties = Properties.objects.all()
    propimgs = PropImages.objects.filter(propImgUrl__contains='_00').order_by("propertyId_id")
    context = {'properties': properties, 'propimgs': propimgs}
    return render(request, 'search/search.html', context)