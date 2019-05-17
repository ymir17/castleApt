from django.shortcuts import render

# Create your views here.

def index(request):
    # print(request)
    # if request.method == 'GET':
    #     print(request.GET)
    #     context = {
    #         # 'credit_card': request.GET.get('credit')
    #     }
    return render(request, 'Paymentreview/paymentreview.html')