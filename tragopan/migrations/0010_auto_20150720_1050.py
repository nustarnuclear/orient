# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0009_auto_20150720_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cycle',
            name='cycle_length',
            field=models.DecimalField(decimal_places=3, max_digits=7, null=True, help_text='unit:EFPD', blank=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='cycle',
            name='shutdown_date',
            field=models.DateField(blank=True, null=True, help_text='Please use <b>YYYY-MM-DD<b> to input the date'),
        ),
        migrations.AlterField(
            model_name='cycle',
            name='starting_date',
            field=models.DateField(blank=True, null=True, help_text='Please use <b>YYYY-MM-DD<b> to input the date'),
        ),
    ]
