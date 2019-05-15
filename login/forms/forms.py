from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        exclude = ['id', 'username']
        widgets = {
            'email': widgets.TextInput(attrs={
                'id': 'e-mail',
                'class': 'inputs',
                'placeholder': 'Email',
            }),
            'password': widgets.PasswordInput(attrs={
                'id': 'pass-word',
                'class': 'inputs',
                'placeholder': 'Password',
            })
        }
