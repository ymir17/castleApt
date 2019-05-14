from django.core.exceptions import ValidationError
<<<<<<< HEAD
from django import forms
from django.forms import ModelForm, widgets
=======
from django.forms import ModelForm, forms, widgets
from django import forms
>>>>>>> 86b65efda2a86a9f80ea2bf9be255fca9cbbbbb4
from signup.models import Accounts, Users


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
<<<<<<< HEAD
            # 're-enter_pw': widgets.PasswordInput(attrs={'class': 'inputs', 'placeholder': 'Re-enter Password'}),
        }
    # pw_validation = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'inputs',
    #                                                                               'placeholder': 'Re-enter Password'}))
    #
    # def is_pw_valid(self):
    #     pw1 = self.Meta.widgets['password']
    #     return pw1 == self.pw_validation
=======
            #'re-enter_pw': widgets.PasswordInput(attrs={'class': 'inputs', 'placeholder': 'Re-enter Password'}),
        }
    #pw_validation = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'inputs',
                                                                                #'placeholder': 'Re-enter Password'}))
    def is_pw_valid(self):
        pw1 = self.Meta.widgets['password']
        #pw2 = self.Meta.widgets['re-enter_pw']
        pw2 = self.pw_validation
        return pw1 == pw2
>>>>>>> 86b65efda2a86a9f80ea2bf9be255fca9cbbbbb4


class CreateUserForm(ModelForm):
    class Meta:
        model = Users
        exclude = ['id', 'accountId', 'accountId_id']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'Address'}),
            'city': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'City'}),
            'zipCode': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'Zip Code'}),
            'country': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'Country'}),
        }
