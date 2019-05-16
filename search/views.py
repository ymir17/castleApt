from django.db.models import Q, Max, Min
from django.shortcuts import render, redirect, get_object_or_404
from property.models import Properties, PropImages
<<<<<<< HEAD
from contacts.models import Realtors
from signup.models import Accounts
from search.forms.forms import searchForm
=======

from contacts.models import Realtors
from signup.models import Accounts
from contacts.models import Realtors
from signup.models import Accounts
from search.forms.forms import searchForm

>>>>>>> 0a088b5cb820e5817e619843622ef8d3406a529f

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

        for key in q:
            # print(key + ':')
            # print(q[key])
            print(key, end=': ')
            print(type(q[key]))
            if key == 'searchBar' and q[key] == '':
                q[key] = None
            elif type(q[key]) is list:
                continue
            elif q[key] is not None:
                if q[key].isdigit():
                    q[key] = int(q[key])

        print(q)
        if q['searchBar'] == '':
            properties_searchBar = Properties.objects.all()
        else:
            properties_searchBar = Properties.objects.filter(Q(address__icontains=q['searchBar']) |
                                                             Q(zipCode__icontains=q['searchBar']))
        if q['checkboxZip'] == []:
            properties_checkBox = Properties.objects.all()
        else:
            properties_checkBox = Properties.objects.filter(Q(zipCode__icontains=q['checkboxZip']))

        if q['priceL'] is None and q['priceH'] is None:
            properties_prices = Properties.objects.all()
        else:
            if q['priceL'] is None:
                # print(Properties.objects.aggregate(Min('price')))
                properties_prices = Properties.objects.filter(Q(price__gte=Properties.objects.aggregate(Min('price'))) &
                                                              Q(price__lte=(q['priceH']) * 1000))
            elif q['priceH'] is None:
                properties_prices = Properties.objects.filter(Q(price__gte=q['priceL'] * 1000) &
                                                              Q(price__lte=Properties.objects.aggregate(Max('price'))))
            else:
                properties_prices = Properties.objects.filter(Q(price__gte=(q['priceL']*1000)) &
                                                              Q(price__lte=(q['priceH'])*1000))

        if q['sizeL'] is None and q['sizeH'] is None:
            properties_sizes = Properties.objects.all()
        else:
            if q['sizeL'] is None:
                properties_sizes = Properties.objects.filter(Q(size__gte=Properties.objects.aggregate(Min('size'))) &
                                                             Q(size__lte=q['sizeH']))
            elif q['sizeH'] is None:
                properties_sizes = Properties.objects.filter(Q(size__gte=q['sizeL']) &
                                                             Q(size__gte=Properties.objects.aggregate(Max('size'))))
            else:
                properties_sizes = Properties.objects.filter(Q(size__gte=q['sizeL']) &
                                                             Q(size__lte=q['sizeH']))

        if q['roomL'] is None and q['roomH'] is None:
            properties_rooms = Properties.objects.all()
        else:
            if q['roomL'] is None:
                properties_rooms = Properties.objects.filter(Q(rooms__gte=Properties.objects.aggregate(Min('rooms'))) &
                                                             Q(rooms__lte=q['roomH']))
            elif q['roomH'] is None:
                properties_rooms = Properties.objects.filter(Q(rooms__gte=q['roomL']) &
                                                             Q(rooms__lte=Properties.objects.aggregate(Max('rooms'))))
            else:
                properties_rooms = Properties.objects.filter(Q(rooms__gte=q['roomL']) &
                                                             Q(rooms_lte=q['roomH']))

        if q['types'] == []:
            properties_types = Properties.objects.all()
        else:
            properties_types = Properties.objects.filter(Q(description=q['types']))

        properties = properties_searchBar.intersection(
            properties_checkBox,
            properties_prices,
            properties_sizes,
            properties_rooms,
            properties_types
        )
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