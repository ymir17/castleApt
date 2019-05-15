from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django import forms
from signup.forms import forms
from signup.forms.forms import CreateAccountForm, CreateUserForm, SignUpForm
from signup.models import Accounts, Users


def signup(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return render(request, 'Sign_up/signup.html', {
        'form': UserCreationForm()
    })


def index(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        newAccount = CreateAccountForm()
        newUser = CreateUserForm(data=request.POST)
        if form.is_valid() and newUser.is_valid():
            newAccount.fields['lastName'] = form.cleaned_data['last_name']
            newAccount.fields['firstName'] = form.cleaned_data['first_name']
            newAccount.fields['email'] = form.cleaned_data['email']
            newAccount.fields['password'] = form.cleaned_data['password1']
            # print(newAccount.data)
            # print(form.data)
            # print(newAccount.is_bound)
            # if newAccount.is_valid():
            form.save()
                # newAccount.save()
            newUser.save()
            return redirect('home-index')
        # if newAccount.is_valid():
        #     newAccount.save()
        #     if newUser.is_valid():
        #         newUser.save()
        #         return redirect('home-index')
        else:
            print("NOT VALID")
            pass
    else:
        form = SignUpForm()
        # newAccount = CreateAccountForm()
        newUser = CreateUserForm()
    return render(request, 'Sign_up/signup.html', {
        'form': form,
        'userForm': newUser,
        # 'form': newAccount, 'form2': newUser
    })

def randomUserName(form):
    pass