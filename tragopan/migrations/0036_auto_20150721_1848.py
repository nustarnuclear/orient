# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0035_auto_20150721_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelassemblyloadingpattern',
            name='fuel_assembly',
            field=models.ForeignKey(default=1, to='tragopan.FuelAssemblyRepository'),
        ),
    ]
