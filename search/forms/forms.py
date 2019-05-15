from django import forms
from django.forms import ModelForm

ZIP_CODES = [
    ('109', '109 Reykjavik'),
    ('112', '112 Reykjavik'),
    ('220', '220 Hafnafjörður'),
    ('311', '311 Borgarnes'),
    ('531', '531 Hvammstangi'),
    ('670', '670 Kópasker'),
    ('740', '740 Neskaupstaður'),
    ('870', '870 Vík'),
    ('109', '109 Reykjavik'),
    ('112', '112 Reykjavik'),
    ('220', '220 Hafnafjörður'),
    ('311', '311 Borgarnes'),
    ('531', '531 Hvammstangi'),
    ('670', '670 Kópasker'),
    ('740', '740 Neskaupstaður'),
    ('870', '870 Vík'),
]
PRICES = [
    ('1', '1'),
    ('2', '2'),
    ('5', '5'),
    ('10', '10'),
    ('15', '15'),
    ('20', '20'),
    ('30', '30'),
    ('40', '40'),
    ('50', '50'),
]
SIZES = [
    ('40', '40'),
    ('50', '50'),
    ('60', '60'),
    ('70', '70'),
    ('80', '80'),
    ('90', '90'),
    ('100', '100'),
    ('150', '150'),
    ('200', '200'),
    ('300', '300'),
    ('400', '400'),
    ('600', '600'),
    ('800', '800'),
    ('1000', '1000'),
]
ROOMS = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('10', '10'),
    ('20', '20'),
    ('30', '30'),
    ('40', '40'),
    ('50', '50'),
    ('75', '75'),
    ('100', '100'),
    ('150', '150'),
]
TYPES = [
    ('castle', 'Castle'),
    ('villa', 'Villa'),
    ('cabin', 'Cabin'),
]


class searchForm(forms.Form):
    searchBar = forms.CharField(
        required=False,
        widget=forms.TextInput,
    )
    checkboxZip = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxInput,
        choices=ZIP_CODES,
    )
    pricesLow = forms.CharField(
        required=False,
        widget=forms.Select(choices=PRICES,),
    )
    pricesHigh = forms.CharField(
        required=False,
        widget=forms.Select(choices=PRICES,),
    )
    sizesLow = forms.CharField(
        required=False,
        widget=forms.Select(choices=SIZES,),
    )
    sizesHigh = forms.CharField(
        required=False,
        widget=forms.Select(choices=SIZES,),
    )
    roomsLow = forms.CharField(
        required=False,
        widget=forms.Select(choices=ROOMS,),
    )
    roomsHigh = forms.CharField(
        required=False,
        widget=forms.Select(choices=ROOMS,),
    )
    types = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TYPES,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['searchBar'].widget.attrs.update({
            'class': 'searchfield',
            'placeholder': 'Type in address, city or town',
            'name': 'search',
            'type': 'text',
        })
        self.fields['checkboxZip'].widget.attrs.update({
            'class': 'container',
        })
        self.fields['pricesLow'].widget.attrs.update({
            'class': 'container',
        })
        self.fields['pricesHigh'].widget.attrs.update({
            'class': 'container',
        })
        self.fields['sizesLow'].widget.attrs.update({
            'class': 'container',
        })
        self.fields['sizesHigh'].widget.attrs.update({
            'class': 'container',
        })
        self.fields['roomsLow'].widget.attrs.update({
            'class': 'container',
        })
        self.fields['roomsHigh'].widget.attrs.update({
            'class': 'container',
        })
        self.fields['types'].widget.attrs.update({
            'class': 'container',
        })
