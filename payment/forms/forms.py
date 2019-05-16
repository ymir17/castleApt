from django import forms
from django.forms import ModelForm

CARD_TYPE = [
    ('Visa', 'visa'),
    ('Mastercard', 'mastercard'),
    ('American Express', 'american express')
]

class PaymentForm(forms.Form):
    cardTypes = forms.Multi