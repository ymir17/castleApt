from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from signup.forms import accountForm
from signup.forms.accountForm import CreateAccountForm, CreateUserForm
from signup.models import Accounts, Users


def index(request):
    return render(request, 'Sign_up/signup.html')


def getUser(request):
    pass


def createUser(request):
    # TODO: Try to implement single form to two separate models! 
    if request.method == 'POST':
        print(request.method)
        newAccount = CreateAccountForm(data=request.POST)
        newUsert = CreateUserForm(data=request.POST)
        if accountForm.is_pw_valid():
            if accountForm.is_valid():
                form = inlineformset_factory(Accounts, Users, fields=('accountId',))
                account = accountForm.save()
                return redirect()
        else:
            pass
    else:
        print(request.method)

        form = CreateAccountForm()
    return render(request, 'base.html', {
        'form': form
    })
