from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django import forms
from signup.forms import accountForm
from signup.forms.accountForm import CreateAccountForm, CreateUserForm
from signup.models import Accounts, Users


def index(request):
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
        else:
            print("NOT VALID")
            pass
    else:
        print(request.method)
        newUsert = CreateUserForm()
        form = CreateAccountForm()
    return render(request, 'Sign_up/signup.html', {

        'form': form, 'form2': newUsert
    })
def getUser(request):
    pass



