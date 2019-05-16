from random import choice
from string import ascii_letters
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Max
from django.forms import ModelForm, widgets
from signup.models import Accounts, Users


class SignUpForm(UserCreationForm):
    last_name = forms.CharField(required='*', widget=forms.TextInput(attrs={
        'class': 'inputs',
        'placeholder': 'Last Name',
    }))
    first_name = forms.CharField(required='*', widget=forms.TextInput(attrs={
        'class': 'inputs',
        'placeholder': 'First Name',
    }))

    randomUsername = ''.join([choice(ascii_letters) for _ in range(30)])
    username = forms.CharField(required='*', widget=forms.HiddenInput(attrs={
        'style': 'display: "hidden"',
        'value': randomUsername,
    }))

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'password1', 'password2')
        widgets = {
            'email': widgets.EmailInput(attrs={'class': 'inputs', 'placeholder': 'Email'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'inputs'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].help_text = None
        self.fields['password2'].widget.attrs['class'] = 'inputs'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter Password'
        self.fields['password2'].help_text = None
        self.fields['username'].errorlist = None

    def save(self, commit=True):
        newAccount = Accounts(lastName=self.cleaned_data['last_name'],
                              firstName=self.cleaned_data['first_name'],
                              email=self.cleaned_data['email'],
                              password=self.cleaned_data['password1'])
        newAccount.save()
        return super(SignUpForm, self).save()


class CreateAccountForm(ModelForm):
    class Meta:
        model = Accounts
        exclude = ['accountId']
        widgets = {
            'lastName': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'Last Name'}),
            'firstName': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'First Name'}),
            'phoneNo': widgets.NumberInput(attrs={'class': 'inputs', 'placeholder': 'Phone Number'}),
            'email': widgets.EmailInput(attrs={'class': 'inputs', 'placeholder': 'Email'}),
            'password': widgets.PasswordInput(attrs={'class': 'inputs', 'placeholder': 'Password'}),
        }


class CreateUserForm(ModelForm):
    class Meta:
        model = Users
        exclude = ['id', 'accountId', 'user']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'Address'}),
            'city': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'City'}),
            'zipCode': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'Zip Code'}),
            'country': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'Country'}),
        }

    def save(self, *args, **kwargs):
        accountId = Accounts.objects.latest('accountId').accountId
        account = Accounts.objects.get(accountId=accountId)
        userMail = User.objects.latest('email').email
        userId = User.objects.get(email=userMail).id

        newUser = Users.objects.create(
            address=self.data['address'],
            city=self.data['city'],
            zipCode=self.data['zipCode'],
            country=self.data['country'],
            accountId=account,
            user_id=userId,
        )
        newUser.save()