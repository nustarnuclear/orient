# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0019_auto_20150720_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuelelementmap',
            name='fuel_assembly_position',
        ),
        migrations.RemoveField(
            model_name='fuelelementmap',
            name='fuel_element_type',
        ),
        migrations.RemoveField(
            model_name='guidtubemap',
            name='guid_tube',
        ),
        migrations.RemoveField(
            model_name='instrumenttubeposition',
            name='guid_tube',
        ),
        migrations.DeleteModel(
            name='FuelElementMap',
        ),
    ]
