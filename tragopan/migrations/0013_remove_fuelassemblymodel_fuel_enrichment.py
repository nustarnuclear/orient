# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0012_fuelassemblymodel_fuel_enrichment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuelassemblymodel',
            name='fuel_enrichment',
        ),
    ]
