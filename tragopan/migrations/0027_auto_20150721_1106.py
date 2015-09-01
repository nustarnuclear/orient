# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0026_auto_20150721_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelelement',
            name='active_length',
            field=models.DecimalField(max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fuelelement',
            name='filling_gas_materia',
            field=models.ForeignKey(blank=True, null=True, to='tragopan.Material'),
        ),
        migrations.AlterField(
            model_name='fuelelement',
            name='filling_gas_pressure',
            field=models.DecimalField(max_digits=10, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:MPa', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fuelelement',
            name='plenum_length',
            field=models.DecimalField(max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', blank=True, null=True),
        ),
    ]
