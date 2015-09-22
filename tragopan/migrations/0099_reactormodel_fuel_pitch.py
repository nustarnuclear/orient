# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0098_auto_20150919_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactormodel',
            name='fuel_pitch',
            field=models.DecimalField(blank=True, help_text='unit:cm', max_digits=7, validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, null=True),
        ),
    ]
