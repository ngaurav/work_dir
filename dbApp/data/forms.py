from django import forms
from django.contrib.auth.models import User
from .models import Client, Page

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('address', 'city', 'pro', 'pic', 'contact')

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ('verified')
