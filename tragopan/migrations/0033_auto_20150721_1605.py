# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0032_auto_20150721_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuelassemblyrepository',
            name='model',
        ),
        migrations.AddField(
            model_name='fuelassemblyrepository',
            name='type',
            field=models.ForeignKey(default=1, to='tragopan.FuelAssemblyType'),
            preserve_default=False,
        ),
    ]
