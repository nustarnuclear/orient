# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0042_auto_20150728_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='burnablepoisonrodmap',
            old_name='guid_tube_position',
            new_name='burnable_poison_position',
        ),
        migrations.RemoveField(
            model_name='burnablepoisonrodmap',
            name='burnable_poison_rod',
        ),
        migrations.AddField(
            model_name='burnablepoisonrod',
            name='fuel_assembly_model',
            field=models.OneToOneField(default=1, to='tragopan.FuelAssemblyModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='controlrodtype',
            name='fuel_assembly_model',
            field=models.ForeignKey(default=1, to='tragopan.FuelAssemblyModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nozzleplugrod',
            name='fuel_assembly_model',
            field=models.OneToOneField(default=1, to='tragopan.FuelAssemblyModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sourcerodtype',
            name='fuel_assembly_model',
            field=models.ForeignKey(default=1, to='tragopan.FuelAssemblyModel'),
            preserve_default=False,
        ),
    ]
