from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from signup.forms.forms import CreateAccountForm, CreateUserForm, SignUpForm


def index(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        newAccount = CreateAccountForm()
        newUser = CreateUserForm(data=request.POST)
        if form.is_valid() and newUser.is_valid():
            formMail = form.cleaned_data['email']
            formPw = form.cleaned_data['password1']
            newAccount.fields['lastName'] = form.cleaned_data['last_name']
            newAccount.fields['firstName'] = form.cleaned_data['first_name']
            newAccount.fields['email'] = form.cleaned_data['email']
            form.save()
            newAccount.fields['password'] = User.objects.get(email=formMail).password # form.cleaned_data['password1']
            newUser.save()
            username = User.objects.get(email=formMail).get_username()
            user = authenticate(request, username=username, password=formPw)
            login(request, user)
            return redirect('home-index')
    else:
        form = SignUpForm()
        newUser = CreateUserForm()
    return render(request, 'Sign_up/signup.html', {
        'form': form,
        'userForm': newUser,
    })