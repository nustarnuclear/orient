# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0093_fuelassemblyrepository_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuelassemblyloadingpattern',
            name='dragable',
        ),
        migrations.AlterField(
            model_name='fuelassemblyloadingpattern',
            name='cycle',
            field=models.ForeignKey(to='tragopan.Cycle', related_name='fuel_assembly_loading_patterns'),
        ),
    ]
