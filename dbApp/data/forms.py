from django import forms
from django.contrib.auth.models import User
from .models import Client, RegularUser, ProUser, Page, Event, Disease, Record, Review
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import SplitDateTimeWidget

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('address', 'city', 'pro', 'pic', 'contact', )

class RegularUserForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=SelectDateWidget())
    class Meta:
        model = RegularUser
        exclude = ('client', )

class ProUserForm(forms.ModelForm):
    class Meta:
        model = ProUser
        exclude = ('client', 'page',)

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('name', 'image',)

class PageContactForm(forms.ModelForm):
    verified = forms.BooleanField(widget=forms.HiddenInput(), initial=True)
    class Meta:
        model = Page
        fields = ('name', 'image', 'contact_details', 'verified')

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ('common_name', 'medical_name', 'description', )

class EventForm(forms.ModelForm):
    start_date = forms.DateField(widget=SelectDateWidget())
    end_date = forms.DateField(widget=SelectDateWidget())
    class Meta:
        model = Event
        fields = ('start_date', 'end_date', 'city', 'disease', )

class RecordForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget())
    class Meta:
        model = Record
        fields = ('date', 'page', 'description', )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ( 'comments', 'disease', 'rating', )