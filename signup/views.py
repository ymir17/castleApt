from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from signup.forms.forms import CreateAccountForm, CreateUserForm, SignUpForm


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
            form.save()
            newUser.save()
            return redirect('login-index')
    else:
        form = SignUpForm()
        newUser = CreateUserForm()
    return render(request, 'Sign_up/signup.html', {
        'form': form,
        'userForm': newUser,
    })