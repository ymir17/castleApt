from django.core.exceptions import FieldError
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from login.forms.forms import LoginForm

def index(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            try:
                username = User.objects.get(email=form.cleaned_data['email']).get_username()
                user = authenticate(request, username=username, password=form.cleaned_data['password'])
            except User.DoesNotExist:
                return render(request, 'Log_in/login.html', {
                    'form': LoginForm(),
                    'login_error': 'Invalid login credentials!',
                })
            if user is not None:
                login(request, user)
                return redirect('home-index')
            else:
                return render(request, 'Log_in/login.html', {
                    'form': LoginForm(),
                    'login_error': 'Invalid login credentials!',
                })
    else:
        form = LoginForm()
    return render(request, 'Log_in/login.html', {
        'form': form,
    })