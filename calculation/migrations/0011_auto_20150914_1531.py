# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0010_auto_20150914_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basefuelcomposition',
            name='height',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, help_text='cm', max_digits=10),
        ),
    ]
