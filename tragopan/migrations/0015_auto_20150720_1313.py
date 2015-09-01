# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0014_fuelassemblycomputemodel_fuelassemblycomputerepository'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FuelAssemblyComputeRepository',
            new_name='FuelAssemblyRepositoryCompute',
        ),
    ]
