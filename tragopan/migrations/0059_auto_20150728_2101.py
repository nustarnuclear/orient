# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0058_auto_20150728_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gridposition',
            name='height',
            field=models.DecimalField(max_digits=10, decimal_places=5, help_text='unit:cm Base on bottom of fuel', validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
