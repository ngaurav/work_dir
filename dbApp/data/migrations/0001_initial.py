# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'City Name')),
                ('country_code', models.PositiveSmallIntegerField(verbose_name=b'Country Code')),
                ('long', models.DecimalField(verbose_name=b'Longitude', max_digits=8, decimal_places=3)),
                ('lat', models.DecimalField(verbose_name=b'Latitude', max_digits=8, decimal_places=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=20, verbose_name=b'Address')),
                ('pro', models.BooleanField(default=False)),
                ('pic', models.ImageField(null=True, upload_to=b'user_images', blank=True)),
                ('contact', models.CharField(max_length=15, verbose_name=b'Contact Number')),
                ('city', models.ForeignKey(to='data.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('common_name', models.CharField(max_length=20, verbose_name=b'Common Name')),
                ('medical_name', models.CharField(max_length=40, verbose_name=b'Medical Name')),
                ('description', models.TextField(default=b'', help_text=b'placeholder for symptoms and prevention measures', max_length=512)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(verbose_name=b'Start Date')),
                ('end_date', models.DateField(verbose_name=b'End Date')),
                ('city', models.ForeignKey(to='data.City')),
                ('client', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('disease', models.ForeignKey(to='data.Disease')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'Display Name')),
                ('verified', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to=b'page_images', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specialization_details', models.TextField(default=b'', help_text=b'Qualifications or Specialization of the Doctor. If the account is for an Institute then, provide the running departments.', max_length=256, verbose_name=b'Specialization Details')),
                ('client', models.ForeignKey(to='data.Client')),
                ('page', models.OneToOneField(null=True, blank=True, to='data.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(default=b'', max_length=512)),
                ('event', models.ForeignKey(to='data.Event')),
                ('page', models.ForeignKey(blank=True, to='data.Page', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegularUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField(verbose_name=b'DOB')),
                ('male_gender', models.BooleanField(default=False)),
                ('client', models.ForeignKey(to='data.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.TextField(default=b'', max_length=512)),
                ('date', models.DateField(auto_now=True)),
                ('rating', models.PositiveSmallIntegerField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('disease', models.ForeignKey(to='data.Disease')),
                ('page', models.ForeignKey(to='data.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
