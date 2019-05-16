from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from property.models import Properties, PropImages
<<<<<<< HEAD
from contacts.models import Realtors
from signup.models import Accounts
=======

from contacts.models import Realtors
from signup.models import Accounts

>>>>>>> 7b786a6bbe5b0955ce183180cf56b8fb069f9614
from search.forms.forms import searchForm


SORT_BY = (
    'Price Low',
    'Price High',
    'Name',
    'Zip Code'
)


def index(request):
    if request.method == 'GET':
        q = {
            'searchBar': request.GET.get('search'),
            'checkboxZip': request.GET.getlist('checkboxZip'),
            'priceL': request.GET.get('pricesLow'),
            'priceH': request.GET.get('pricesHigh'),
            'sizeL': request.GET.get('sizesLow'),
            'sizeH': request.GET.get('sizesHigh'),
            'roomL': request.GET.get('roomsLow'),
            'roomH': request.GET.get('roomsHigh'),
            'types': request.GET.getlist('types')
        }
        print(q)
        properties_searchBar = Properties.objects.filter(Q(address__icontains=q['searchBar']) |
                                               Q(zipCode__icontains=q['searchBar']))
        properties_checkBox = Properties.objects.filter(Q(zipCode__icontains=q['checkboxZip']))
        properties_prices = Properties.objects.filter(Q(price__gte=39840000))
        properties = properties_prices
        print(properties)
        propimgs = PropImages.objects.filter(propImgUrl__contains='_00').order_by("propertyId_id")
        context = {'properties': properties, 'propimgs': propimgs}
        return render(request, 'search/search.html', context)
    return redirect('home-index')


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