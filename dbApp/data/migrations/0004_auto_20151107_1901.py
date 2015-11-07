# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_page_contact_details'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterField(
            model_name='client',
            name='pro',
            field=models.BooleanField(default=False, help_text=b'Check only for professional accounts', verbose_name=b'Professional account'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
