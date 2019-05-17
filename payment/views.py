from django.shortcuts import render, get_object_or_404

from payment.forms import forms
from property.models import Properties, PropImages
from payment.forms.forms import PaymentForm
from contacts.models import Realtors
from signup.models import Accounts, Users


def index(request, id):
    return render(request, 'Payment/payment.html', {
        'form': PaymentForm(data=request.GET),
        'property': get_object_or_404(Properties, pk=id),
        'images': PropImages.objects.filter(propImgUrl__contains='_00').order_by("propertyId_id"),
        'userInfo': userInfo(request.user.id),
        'countries': forms.COUNTRIES,
    })


def userInfo(id):
    user = Users.objects.get(user_id=id)
    q = {
        'address': user.address,
        'city': user.city,
        'country': user.country.capitalize(),
        'zip': user.zipCode,
    }
    return q

def paymentReview(request, id):
    return render(request, 'Paymentreview/paymentreview.html', {
        'property': get_object_or_404(Properties, pk=id),
        'images': PropImages.objects.filter(propImgUrl__contains='_00').order_by("propertyId_id"),
        'realtors': Realtors.objects.all(),
        'accounts': Accounts.objects.all()
    })
