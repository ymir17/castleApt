from django.shortcuts import render, redirect
from django.http import Http404
from contacts.models import Realtors, RealtorImages
from signup.models import Accounts


def index(request):
    realtorImg = RealtorImages.objects.all().order_by("realtImgUrl")
    account = Accounts.objects.all().order_by("firstName")
    realtor = Realtors.objects.all()
    context = {'accounts': account, 'realtorImgs': realtorImg, 'realtors': realtor}
    return render(request, 'Contacts/contacts.html', context)



# def getRealtors(request, id):
#     if id == Realtors.objects.get(accountId=id).accountId_id:
#         realtors = {
#             'name': str(Accounts.objects.get(accountId=id).firstName) + ' ' + str(Accounts.objects.get(accountId=id).lastName),
#             'description': str(Realtors.objects.get(accountId=id).description),
#             'phoneNo': str(Accounts.objects.get(accountId=id).phoneNo),
#             'email': str(Accounts.objects.get(accountId=id).email),
#             'image': RealtorImages.objects.get(realtImgId=(Realtors.objects.get(accountId=id).realtImgId_id)).realtImgUrl
#         }
#
#         return render(request, realtors)
#     raise Http404('Realtor does not exists')
