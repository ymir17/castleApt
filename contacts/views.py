from django.shortcuts import render, redirect
from contacts.models import Realtors, RealtorImages
from signup.models import Accounts



# Create your views here.
def index(request):
    realtorimg = RealtorImages.objects.all().order_by("realtImgUrl")
    realtors = Accounts.objects.all().order_by("firstName")
    context = {'data': realtorimg, 'realtors': realtors}
    return render(request, 'Contacts/contacts.html', context)