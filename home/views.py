from django.shortcuts import render

ZIP_CODES = (
    '109 Reykjavik',
    '112 Reykjavik',
    '220 Hafnafjörður',
    '311 Borgarnes',
    '531 Hvammstangi',
    '670 Kópasker',
    '740 Neskaupstaður',
    '870 Vík',
    '109 Reykjavik',
    '112 Reykjavik',
    '220 Hafnafjörður',
    '311 Borgarnes',
    '531 Hvammstangi',
    '670 Kópasker',
    '740 Neskaupstaður',
    '870 Vík',
)
PRICES = (
    '1',
    '2',
    '5',
    '10',
    '15',
    '20',
    '30',
    '40',
    '50',
)
SIZES = (
    '40',
    '50',
    '60',
    '70',
    '80',
    '90',
    '100',
    '150',
    '200',
    '300',
    '400',
    '600',
    '800',
    '1000',
)
ROOMS = (
    '1',
    '2',
    '3',
    '4',
    '5',
    '10',
    '20',
    '30',
    '40',
    '50',
    '75',
    '100',
    '150',
)
TYPES = (
    'Castle',
    'Villa',
    'Cabin',
)


def searchForm():
    pass


<<<<<<< HEAD

# Create your views here.
=======
>>>>>>> b79d98b505b103a5abb169a5a07d236e749e5b6e
def index(request):
    return render(request, 'Home/home.html')