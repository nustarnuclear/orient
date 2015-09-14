# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0096_auto_20150911_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grid',
            name='fuel_assembly_model',
            field=models.ForeignKey(related_name='fuel_assembly_grids', to='tragopan.FuelAssemblyModel'),
        ),
    ]
