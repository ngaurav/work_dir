from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name="Diaplay Name")
    country_code = models.PositiveSmallIntegerField(blank=False, null=False, verbose_name="Country Code")
    long = models.DecimalField(null=False, blank=False, max_digits=8, decimal_places=3, verbose_name="Longitude")
    lat = models.DecimalField(null=False, blank=False, max_digits=8, decimal_places=3, verbose_name="Latitude")

class Client(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    address = models.CharField(max_length=20, blank=False, null=False, verbose_name="Address")
    city = models.ForeignKey(City, null=False, blank=False)
    pro = models.BooleanField(default=False)
    pic = models.ImageField(null=True, blank=True, upload_to='user_images')
    contact = models.CharField(max_length=15, blank=False, null=False, verbose_name="Contact Number")

class RegularUser(models.Model):
    client = models.ForeignKey(Client, null=False, blank=False)
    date_of_birth = models.DateField(blank=False, null=False, verbose_name="DOB")
    male_gender = models.BooleanField(default=False)

class Page(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name="Display Name")
    verified = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to='page_images')

class ProUser(models.Model):
    client = models.ForeignKey(Client, null=False, blank=False)
    specialization_details = models.TextField(max_length = 256,
        default='', help_text="Qualifications or Specialization of the Doctor. If the account is for an Institute then, provide the running departments.",
        verbose_name="Specialization Details")
    page = models.OneToOneField(Page, null=True, blank=True)

class Disease(models.Model):
    common_name = models.CharField(max_length=20, blank=False, null=False, verbose_name="Diaplay Name")
    medical_name = models.CharField(max_length=20, blank=False, null=False, verbose_name="Medical Name")
    description = models.TextField(max_length = 512,
        default='', help_text="placeholder for symptoms and prevention measures")

class Event(models.Model):
    start_date = models.DateField(blank=False, null=False, verbose_name="Start Date")
    end_date = models.DateField(blank=False, null=False, verbose_name="End Date")
    city = models.ForeignKey(City, null=False, blank=False)
    disease = models.ForeignKey(Disease, null=False, blank=False)
    client = models.ForeignKey(RegularUser, null=False, blank=False)

class Record(models.Model):
    timestamp = models.DateTimeField(null=False, blank=False)
    event = models.ForeignKey(Event, null=False, blank=False)
    page = models.ForeignKey(Page, null=True, blank=True)

class Review(models.Model):
    author = models.ForeignKey(RegularUser, null=False, blank=False)
    comments = models.TextField(max_length = 512, default='')
    date = models.DateTimeField(editable = True, auto_now=True)
    page = models.ForeignKey(Page, null=False, blank=False)
    disease = models.ForeignKey(Disease, null=False, blank=False)
    rating = models.PositiveSmallIntegerField(null=False, blank=False)
