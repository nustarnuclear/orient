# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0041_auto_20150727_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='burnablepoisonassemblynozzleplug',
            name='burnable_poison_assembly',
        ),
        migrations.RemoveField(
            model_name='burnablepoisonassemblynozzleplug',
            name='guid_tube_position',
        ),
        migrations.RemoveField(
            model_name='burnablepoisonassemblynozzleplug',
            name='nozzle_plug_rod',
        ),
        migrations.RemoveField(
            model_name='burnablepoisonassembly',
            name='nozzle_plug_rod_map',
        ),
        migrations.AddField(
            model_name='burnablepoisonassembly',
            name='fuel_assembly_model',
            field=models.OneToOneField(to='tragopan.FuelAssemblyModel', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='burnablepoisonrod',
            name='active_length',
            field=models.DecimalField(max_digits=7, default=1, validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, help_text='unit:cm'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BurnablePoisonAssemblyNozzlePlug',
        ),
    ]
