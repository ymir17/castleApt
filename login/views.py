from django.shortcuts import render
from login.forms.forms import LoginForm


def index(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            pass
    else:
        form = LoginForm()
    return render(request, 'Log_in/login.html', {
        'form': form,
    })