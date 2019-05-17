from django import forms
from django.forms import ModelForm
from editprofile.views import *
from django.contrib.auth.models import User
from login.forms.forms import LoginForm

class editProfileForm(forms.Form):
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput,
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput,
    )
    email = forms.CharField(
        required=False,
        widget=forms.TextInput,
    )
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
    )
    repassword = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
    )
    phoneNumber = forms.IntegerField(
        required=False,
        widget=forms.TextInput,
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput,
    )
    city = forms.CharField(
        required=False,
        widget=forms.TextInput,
    )
    zipCode = forms.IntegerField(
        required=False,
        widget=forms.TextInput,
    )
    country = forms.CharField(
        required=False,
        widget=forms.TextInput,
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'inputs',
            'name': 'firstname',
            'type': 'text',
            'readonly': 'readonly',
            'id': 'first-name',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'inputs',
            'name': 'lastname',
            'type': 'text',
            'readonly': 'readonly',
            'id': 'last-name',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'inputs',
            'name': 'email',
            'type': 'text',
            'readonly': 'readonly',
            'id': 'e-mail',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'inputs',
            'name': 'password',
            'type': 'password',
            'readonly': 'readonly',
            'id': 'pass-word',
        })
        self.fields['repassword'].widget.attrs.update({
            'class': 'inputs',
            'name': 'repassword',
            'type': 'password',
            'readonly': 'readonly',
            'id': 're-password',
        })
        self.fields['phoneNumber'].widget.attrs.update({
            'class': 'inputs',
            'name': 'phonenumber',
            'type': 'number',
            'readonly': 'readonly',
            'id': 'phone-number',
        })
        self.fields['address'].widget.attrs.update({
            'class': 'inputs',
            'name': 'address',
            'type': 'text',
            'readonly': 'readonly',
            'id': 'address',
        })
        self.fields['city'].widget.attrs.update({
            'class': 'inputs',
            'name': 'city',
            'type': 'text',
            'readonly': 'readonly',
            'id': 'city',
        })
        self.fields['zipCode'].widget.attrs.update({
            'class': 'inputs',
            'name': 'zipcode',
            'type': 'number',
            'readonly': 'readonly',
            'id': 'zipcode',
        })
        self.fields['country'].widget.attrs.update({
            'class': 'inputs',
            'name': 'country',
            'type': 'text',
            'readonly': 'readonly',
            'id': 'country',
        })

class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    password = forms.CharField(required=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use.')
        return email

    def save(self, commit=True):
        user = super(LoginForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user