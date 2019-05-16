from django import forms
from django.forms import ModelForm
from django_countries import countries
from django_countries.fields import CountryField

CARD_TYPE = [
    ('Visa', 'visa'),
    ('Mastercard', 'mastercard'),
    ('American Express', 'american express')
]

class PaymentForm(forms.Form):
    cardTypes = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=CARD_TYPE,
    )
    nameOnCard = forms.CharField(
        required=True,
        widget=forms.TextInput,
    )
    cardNumber = forms.IntegerField(
        required=True,
        widget=forms.TextInput,
    )
    expDate = forms.DateField(
        required=True,
        widget=forms.DateInput,
    )
    cvc = forms.IntegerField(
        required=True,
        widget=forms.TextInput,
    )
    bAddress = forms.CharField(
        required=True,
        widget=forms.TextInput,
    )
    houseNumber = forms.IntegerField(
        required=True,
        widget=forms.TextInput,
    )
    city = forms.CharField(
        required=True,
        widget=forms.TextInput,
    )
    country = forms.ChoiceField(
        required=True,
        choices=list(countries),
    )
    zipCode = forms.IntegerField(
        required=True,
        widget=forms.TextInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cardTypes'].widget.attrs.update({
            'type': 'radio',
            'name': 'card',
        })
        self.fields['nameOnCard'].widget.attrs.update({
            'class': 'inputs',
            'placeholder': 'Name on card',
            'name': 'cardname',
            'type': 'text',
        })
        self.fields['cardNumber'].widget.attrs.update({
            'class': 'inputs',
            'placeholder': 'Card number',
            'name': 'cardnumber',
            'type': 'number',
        })
        self.fields['expDate'].widget.attrs.update({
            'class': 'inputs',
            'placeholder': 'Exp. date',
            'name': 'Exp-date',
            'type': 'date',
        })
        self.fields['cvc'].widget.attrs.update({
            'class': 'inputs',
            'placeholder': 'CVC',
            'name': 'CVC',
            'type': 'number',
        })
        self.fields['bAddress'].widget.attrs.update({
            'class': 'inputs',
            'placeholder': 'Billing address',
            'name': 'address',
            'type': 'text',
        })
        self.fields['houseNumber'].widget.attrs.update({
            'class': 'inputs',
            'placeholder': 'House number',
            'name': 'housenumber',
            'type': 'number',
        })
        self.fields['city'].widget.attrs.update({
            'class': 'inputs',
            'placeholder': 'City',
            'name': 'city',
            'type': 'text',
        })
        self.fields['country'].widget.attrs.update({
            'class': 'inputs',
        })
        self.fields['zipCode'].widget.attrs.update({
            'class': 'inputs',
            'placeholder': 'Postal code',
            'name': 'postalcode',
            'type': 'number',
        })

