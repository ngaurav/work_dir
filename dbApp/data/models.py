from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    pro = models.BooleanField(default=False)

class RegularUser(models.Model):
    client = models.ForiegnKey(Client, null=False, blank=False)
    date_of_birth = models.DateField(blank=False, null=False, verbose_name="DOB")
    male_gender = models.BooleanField(default=False)

class Page(models.Model):
    name = models.CharField(blank=False, null=False, verbose_name="Diaplay Name")
    verified = modls.BooleanField(default=False)

class ProUser(models.Model):
    client = models.ForiegnKey(Client, null=False, blank=False)
    specialization_details = models.TextField(max_length = 256,
        default='', help_text="Qualifications or Specialization of the Doctor. If the account is for an Institute then, provide the running departments.",
        verbose_name="Specialization Details")
    page = models.OneToOneField(Page, null=True, blank=True)

class Disease(models.Model):
    common_name = models.CharField(blank=False, null=False, verbose_name="Diaplay Name")
    medical_name = models.CharField(blank=False, null=False, verbose_name="Medical Name")
    description = models.TextField(max_length = 512,
        default='', help_text="placeholder for symptoms and prevention measures")

class Event(models.Model):
    start_date = models.DateField(blank=False, null=False, verbose_name="Start Date")
    end_date = models.DateField(blank=False, null=False, verbose_name="End Date")
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    disease = models.ForiegnKey(Disease, null=False, blank=False)
    client = models.ForeignKey(RegularUser, null=False, blank=False)

class Record(models.Model):
    timestamp = models.DateTimeField(editable = True, auto_now_add=True)
    event = models.ForiegnKey(Event, null=False, blank=False)
    page = models.ForiegnKey(null=True, blank=True)

class Review(models.Model):
    author = models.ForeignKey(RegularUser, null=False, blank=False)
    comments = models.TextField(max_length = 512, default='')
    date = models.DateTimeField(editable = True, auto_now=True)
    page = models.ForeignKey(Page, null=False, blank=False)
    disease = models.ForeignKey(Page, null=False, blank=False)
    rating = models.PositiveSmallIntegerField(null=False, blank=False)
