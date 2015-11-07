# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20151106_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='contact_details',
            field=models.TextField(max_length=50, null=True, verbose_name=b'Contact Details', blank=True),
            preserve_default=True,
        ),
    ]
