from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django import forms
from signup.forms import accountForm
from signup.forms.accountForm import CreateAccountForm, CreateUserForm
from signup.models import Accounts, Users


def index(request):
<<<<<<< HEAD
    return render(request, 'Sign_up/signup.html')


def createUser(request):
    # TODO: Try to implement single form to two separate models!
    if request.method == 'POST':
        newAccount = CreateAccountForm(data=request.POST)
        newUser = CreateUserForm(data=request.POST)
        form = inlineformset_factory(Accounts, Users, fields=('accountId',))
        # if newAccount.is_pw_valid():
        if newAccount.is_valid() and newUser.is_valid():
            account = newAccount.save()
            user = newUser.save()
            sum = form.save()
            return redirect('home-index')
=======
    # def createUser(request):
    # TODO: Try to implement single form to two separate models!
    if request.method == 'POST':
        print(request.method)
        form = CreateAccountForm(data=request.POST)
        newUsert = CreateUserForm(data=request.POST)
        #if form.is_pw_valid():
        if form.is_valid():
            print("VALID ACCOUNT")
            # form = inlineformset_factory(Accounts, Users, fields=('accountId',))
            form.save()
            if newUsert.is_valid():
                print("VALID USER")
                newUsert.save()
            # account = accountForm.save()
                return redirect('home-index')
>>>>>>> 86b65efda2a86a9f80ea2bf9be255fca9cbbbbb4
        else:
            print("NOT VALID")
            pass
    else:
<<<<<<< HEAD
        form = CreateAccountForm()
    return render(request, 'Sign_up/signup.html', {
        'form': form
=======
        print(request.method)
        newUsert = CreateUserForm()
        form = CreateAccountForm()
    return render(request, 'Sign_up/signup.html', {

        'form': form, 'form2': newUsert
>>>>>>> 86b65efda2a86a9f80ea2bf9be255fca9cbbbbb4
    })
def getUser(request):
    pass



