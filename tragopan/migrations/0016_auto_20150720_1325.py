# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0015_auto_20150720_1313'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FuelAssemblyComputeModel',
        ),
        migrations.RemoveField(
            model_name='fuelassemblyrepositorycompute',
            name='model',
        ),
        migrations.RemoveField(
            model_name='fuelassemblyrepositorycompute',
            name='plant',
        ),
        migrations.DeleteModel(
            name='FuelAssemblyRepositoryCompute',
        ),
    ]
