# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0031_auto_20150721_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelpellet',
            name='coating_thickness',
            field=models.DecimalField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], max_digits=7, help_text='unit:cm', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fuelpellet',
            name='inner_diameter',
            field=models.DecimalField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], max_digits=7, help_text='unit:cm can be none when hollow', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fuelpellet',
            name='length',
            field=models.DecimalField(help_text='unit:cm', decimal_places=5, validators=[django.core.validators.MinValueValidator(0)], max_digits=7),
        ),
        migrations.AlterField(
            model_name='fuelpellet',
            name='outer_diameter',
            field=models.DecimalField(help_text='unit:cm', decimal_places=5, validators=[django.core.validators.MinValueValidator(0)], max_digits=7),
        ),
    ]
