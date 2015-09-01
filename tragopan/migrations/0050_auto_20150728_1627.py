# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0049_auto_20150728_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlrodassembly',
            name='overall_length',
        ),
        migrations.AddField(
            model_name='controlrodassembly',
            name='fuel_assembly_model',
            field=models.ForeignKey(to='tragopan.FuelAssemblyModel', default=1),
            preserve_default=False,
        ),
    ]
