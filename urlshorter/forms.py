from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, TextInput, CharField, EmailField
from django import forms
from .models import Url
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = CharField(label='User name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = CharField(
        label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Password must be at least 8 characters'
    )






class UserRegisterForm(UserCreationForm):
    username = CharField(label='User name', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Enter password',  widget=forms.PasswordInput(attrs={'class':'form-control'}), help_text=
                                'Password must be at least 8 characters')
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']



class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['source_url']
        labels = {
            'source_url': 'Enter your Url'
        }
        error_messages = {
            'source_url':{'max_length': 'to many symbols', 'min_length': 'your url is already short'}
        }
        widgets = {
            'source_url': TextInput(attrs={
                'class': 'todo',
                'placeholder': 'example: https://github.com/ArturZhukovets?tab=repositories'
            })
        }


