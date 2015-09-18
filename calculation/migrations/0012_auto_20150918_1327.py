# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0011_auto_20150914_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='ibis',
            name='active_length',
            field=models.DecimalField(decimal_places=5, help_text='unit:cm', max_digits=10, validators=[django.core.validators.MinValueValidator(0)], default=365.8),
        ),
        migrations.AlterField(
            model_name='basefuelcomposition',
            name='base_fuel',
            field=models.ForeignKey(to='calculation.BaseFuel', related_name='composition'),
        ),
    ]
