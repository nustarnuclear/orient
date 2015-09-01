# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0053_auto_20150728_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sourceassemblybprod',
            name='burnable_poison_rod',
        ),
        migrations.RemoveField(
            model_name='sourceassemblybprod',
            name='guid_tube_position',
        ),
        migrations.RemoveField(
            model_name='sourceassemblybprod',
            name='source_assembly',
        ),
        migrations.RemoveField(
            model_name='sourceassemblynozzleplug',
            name='guid_tube_position',
        ),
        migrations.RemoveField(
            model_name='sourceassemblynozzleplug',
            name='nozzle_plug_rod',
        ),
        migrations.RemoveField(
            model_name='sourceassemblynozzleplug',
            name='source_assembly',
        ),
        migrations.RemoveField(
            model_name='sourceassembly',
            name='burnable_poison_map',
        ),
        migrations.RemoveField(
            model_name='sourceassembly',
            name='nozzle_plug_rod_map',
        ),
        migrations.AddField(
            model_name='sourceassembly',
            name='fuel_assembly_model',
            field=models.ForeignKey(default=1, to='tragopan.FuelAssemblyModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sourcerodmap',
            name='guid_tube_position',
            field=models.ForeignKey(to='tragopan.FuelAssemblyPosition'),
        ),
        migrations.DeleteModel(
            name='SourceAssemblyBPRod',
        ),
        migrations.DeleteModel(
            name='SourceAssemblyNozzlePlug',
        ),
    ]
