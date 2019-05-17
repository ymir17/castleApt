from django import forms
from django.forms import ModelForm


class MailForm(forms.Form):

    name = forms.CharField(
        required=True,
        widget=forms.TextInput,
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput,
    )
    phoneNo = forms.IntegerField(
        required=False,
        widget=forms.NumberInput,
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'id': 'name',
            'placeholder': 'Full Name',
            'class': 'inputs',
            'type': 'text'
        })
        self.fields['email'].widget.attrs.update({
            'id': 'email',
            'placeholder': 'Email Address',
            'class': 'inputs',
            'type': 'text'
        })
        self.fields['phoneNo'].widget.attrs.update({
            'id': 'pnumber',
            'placeholder': 'Phone Number',
            'class': 'inputs',
            'type': 'text'
        })
        self.fields['message'].widget.attrs.update({
            'id': 'subject',
            'placeholder': 'Type in your message here',
        })