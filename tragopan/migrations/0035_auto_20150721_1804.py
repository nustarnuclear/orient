# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0034_auto_20150721_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelassemblyloadingpattern',
            name='fuel_assembly',
            field=models.ForeignKey(blank=True, to='tragopan.FuelAssemblyRepository', null=True),
        ),
    ]
