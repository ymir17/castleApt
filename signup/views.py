from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from signup.forms import accountForm
from signup.forms.accountForm import CreateAccountForm, CreateUserForm
from signup.models import Accounts, Users


def index(request):
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
        else:
            pass
    else:
        form = CreateAccountForm()
    return render(request, 'Sign_up/signup.html', {
        'form': form
    })
