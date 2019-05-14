from random import choice
from string import ascii_letters
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from signup.models import Accounts, Users


class SignUpForm(UserCreationForm):
    # UserCreationForm has:
    # username, password, password confirmation
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'inputs',
        'placeholder': 'Last Name',
    }))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'inputs',
        'placeholder': 'First Name',
    }))

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'password1', 'password2')
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
            # 're-enter_pw': widgets.PasswordInput(attrs={'class': 'inputs', 'placeholder': 'Re-enter Password'}),
        }
    # pw_validation = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'inputs',
    #                                                                               'placeholder': 'Re-enter Password'}))

    def is_pw_valid(self):
        pw1 = self.Meta.widgets['password']
        # pw2 = self.Meta.widgets['re-enter_pw']
        pw2 = self.pw_validation
        return pw1 == pw2


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
