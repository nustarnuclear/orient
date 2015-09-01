# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0011_auto_20150720_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelassemblymodel',
            name='fuel_enrichment',
            field=models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:% U235', blank=True, max_digits=9, null=True, decimal_places=6),
        ),
    ]
