from django import forms
from django.contrib.auth.models import User
from .models import Client, Page, Event, Disease, Record, Review
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

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ('verified', )

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ('common_name', 'medical_name', 'description', )

class EventForm(forms.ModelForm):
    start_date = forms.DateField(widget=SelectDateWidget())
    end_date = forms.DateField(widget=SelectDateWidget())
    class Meta:
        model = Event
        fields = ('start_date', 'end_date', 'city', 'disease', 'client', )

class RecordForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget())
    class Meta:
        model = Record
        fields = ('date', 'event', 'page', 'description', )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('author', 'comments', 'page', 'disease', 'rating', )