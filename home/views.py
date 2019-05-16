from django.shortcuts import render
from search.forms.forms import searchForm


def index(request):
    return render(request, 'Home/home.html', {
        'form': searchForm(data=request.GET)
    })