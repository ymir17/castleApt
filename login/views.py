from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from login.forms.forms import LoginForm

# TODO: except UserDoesNotExists
def index(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = User.objects.get(email=form.cleaned_data['email']).get_username()
            user = authenticate(request, username=username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home-index')
            else:
                print('Not Valid user')
    else:
        form = LoginForm()
    return render(request, 'Log_in/login.html', {
        'form': form,
    })