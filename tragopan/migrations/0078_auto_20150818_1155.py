# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0077_auto_20150818_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelassemblymodel',
            name='assembly_pitch',
            field=models.DecimalField(decimal_places=4, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', default=21.504, max_digits=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gridposition',
            name='fuel_assembly_model',
            field=models.ForeignKey(related_name='grids', to='tragopan.FuelAssemblyModel'),
        ),
    ]
