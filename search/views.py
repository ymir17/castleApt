from django.shortcuts import render, redirect, get_object_or_404
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

def get_prop_by_id(request, id):
    propimgs = PropImages.objects.all().order_by('propImgUrl')
    return render(request, 'Property/property.html', {
        'property': get_object_or_404(Properties, pk=id),
        'images': propimgs
    })