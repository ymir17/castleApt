from django.core.exceptions import ValidationError
from django.forms import ModelForm, forms, widgets
from signup.models import Accounts, Users


class CreateAccountForm(ModelForm):
    class Meta:
        model = Accounts
        exclude = ['accountId']
        widgets = {
            'lastName': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'First Name'}),
            'firsName': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'Last Name'}),
            'email': widgets.EmailInput(attrs={'class': 'inputs', 'placeholder': 'Email'}),
            'password': widgets.PasswordInput(attrs={'class': 'inputs', 'placeholder': 'Password'}),
            're-enter_pw': widgets.PasswordInput(attrs={'class': 'inputs', 'placeholder': 'Re-enter Password'}),
        }

    def is_pw_valid(self):
        pw1 = self.Meta.widgets['password']
        pw2 = self.Meta.widgets['re-enter_pw']
        return pw1 == pw2


class CreateUserForm(ModelForm):
    class Meta:
        model = Users
        exclude = ['id']
        widgets = {
            'phoneNo': widgets.NumberInput(attrs={'class': 'inputs', 'placeholder': 'Phone Number'}),
            'address': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'Address'}),
            'city': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'City'}),
            'zipCode': widgets.TextInput(attrs={'class': 'inputs', 'placeholder': 'Zip Code'}),
            'country': widgets.Select(attrs={'class': 'inputs', 'placeholder': 'Country'}),
        }
