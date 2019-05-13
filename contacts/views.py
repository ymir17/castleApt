from django.shortcuts import render, redirect
from contacts.models import Realtors, RealtorImages
from signup.models import Accounts


def index(request):
    realtorImg = RealtorImages.objects.all().order_by("realtImgUrl")
    account = Accounts.objects.all().order_by("firstName")
    realtor = Realtors.objects.all()
    context = {'accounts': account, 'realtorImgs': realtorImg, 'realtors': realtor}
    return render(request, 'Contacts/contacts.html', context)