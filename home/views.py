from django.shortcuts import render
from search.forms.forms import searchForm


def index(request):
    if request.method == 'POST':
        print('POST')
        # form = searchForm(data=request.POST)
        # if form.is_valid():
        #     pass
    else:
        form = searchForm()
    return render(request, 'Home/home.html', {
        'form': form
    })
