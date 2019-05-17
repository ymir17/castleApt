from django.shortcuts import render


def index(request):
    return render(request, 'Paymentreview/paymentreview.html')