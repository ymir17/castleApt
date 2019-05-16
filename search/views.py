from django.shortcuts import render, redirect, get_object_or_404
from property.models import Properties, PropImages
from contacts.models import Realtors
from signup.models import Accounts

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
    frontimgs = PropImages.objects.filter(propImgUrl__contains='_00').order_by("propertyId_id")
    props = Properties.objects.all()
    realtors = Realtors.objects.all()
    accounts = Accounts.objects.all()
    return render(request, 'Property/property.html', {
        'property': get_object_or_404(Properties, pk=id),
        'images': propimgs,
        'allprops': props,
        'frontimg': frontimgs,
        'realtor': realtors,
        'account': accounts
    })