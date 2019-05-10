from django.shortcuts import render, redirect
from contacts.models import Realtors, RealtorImages
from signup.models import Accounts



# Create your views here.
def index(request):
    realtorimg = {'data': RealtorImages.objects.all()}

    return render(request, 'Contacts/contacts.html', realtorimg)