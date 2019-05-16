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
    ('#', ''),
    ('1', '€1m'),
    ('2', '€2m'),
    ('5', '€5m'),
    ('10', '€10m'),
    ('15', '€15m'),
    ('20', '€20m'),
    ('30', '€30m'),
    ('40', '€40m'),
    ('50', '€50m'),
]
SIZES = [
    ('#', ''),
    ('40', '40 sq. ft'),
    ('50', '50 sq. ft'),
    ('60', '60 sq. ft'),
    ('70', '70 sq. ft'),
    ('80', '80 sq. ft'),
    ('90', '90 sq. ft'),
    ('100', '100 sq. ft'),
    ('150', '150 sq. ft'),
    ('200', '200 sq. ft'),
    ('300', '300 sq. ft'),
    ('400', '400 sq. ft'),
    ('600', '600 sq. ft'),
    ('800', '800 sq. ft'),
    ('1000', '1000 sq. ft'),
]
ROOMS = [
    ('#', ''),
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
        widget=forms.CheckboxSelectMultiple,
        choices=ZIP_CODES,
        label= 'Zip Codes',
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

        })
        self.fields['pricesLow'].widget.attrs.update({
            'class': 'alldropdowns',
        })
        self.fields['pricesHigh'].widget.attrs.update({
            'class': 'alldropdowns',
        })
        self.fields['sizesLow'].widget.attrs.update({
            'class': 'alldropdowns',
        })
        self.fields['sizesHigh'].widget.attrs.update({
            'class': 'alldropdowns',
        })
        self.fields['roomsLow'].widget.attrs.update({
            'class': 'alldropdowns',
        })
        self.fields['roomsHigh'].widget.attrs.update({
            'class': 'alldropdowns',
        })
        self.fields['types'].widget.attrs.update({
            'class': 'container',
        })
