# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0028_auto_20150721_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guidtubemap',
            name='fuel_assembly_position',
        ),
        migrations.RemoveField(
            model_name='instrumenttubeposition',
            name='fuel_assembly_position',
        ),
        migrations.AlterField(
            model_name='burnablepoisonassembly',
            name='burnable_poison_map',
            field=models.ManyToManyField(through='tragopan.BurnablePoisonRodMap', to='tragopan.FuelAssemblyPosition', related_name='bp_burnable_poison'),
        ),
        migrations.AlterField(
            model_name='burnablepoisonassembly',
            name='nozzle_plug_rod_map',
            field=models.ManyToManyField(through='tragopan.BurnablePoisonAssemblyNozzlePlug', to='tragopan.FuelAssemblyPosition', related_name='bp_nozzle_plug'),
        ),
        migrations.AlterField(
            model_name='burnablepoisonassemblynozzleplug',
            name='guid_tube_position',
            field=models.OneToOneField(to='tragopan.FuelAssemblyPosition'),
        ),
        migrations.AlterField(
            model_name='burnablepoisonrodmap',
            name='guid_tube_position',
            field=models.OneToOneField(to='tragopan.FuelAssemblyPosition'),
        ),
        migrations.AlterField(
            model_name='controlrodassembly',
            name='control_rod_map',
            field=models.ManyToManyField(through='tragopan.ControlRodMap', to='tragopan.FuelAssemblyPosition'),
        ),
        migrations.AlterField(
            model_name='controlrodmap',
            name='guid_tube_position',
            field=models.OneToOneField(to='tragopan.FuelAssemblyPosition'),
        ),
        migrations.AlterField(
            model_name='nozzleplugrodmap',
            name='guid_tube_position',
            field=models.OneToOneField(to='tragopan.FuelAssemblyPosition'),
        ),
        migrations.AlterField(
            model_name='sourceassembly',
            name='burnable_poison_map',
            field=models.ManyToManyField(through='tragopan.SourceAssemblyBPRod', to='tragopan.FuelAssemblyPosition', related_name='source_burnable_poison'),
        ),
        migrations.AlterField(
            model_name='sourceassembly',
            name='nozzle_plug_rod_map',
            field=models.ManyToManyField(through='tragopan.SourceAssemblyNozzlePlug', to='tragopan.FuelAssemblyPosition', related_name='source_nozzle_plug'),
        ),
        migrations.AlterField(
            model_name='sourceassembly',
            name='source_rod_map',
            field=models.ManyToManyField(through='tragopan.SourceRodMap', to='tragopan.FuelAssemblyPosition', related_name='source_rod'),
        ),
        migrations.AlterField(
            model_name='sourceassemblybprod',
            name='guid_tube_position',
            field=models.OneToOneField(to='tragopan.FuelAssemblyPosition'),
        ),
        migrations.AlterField(
            model_name='sourceassemblynozzleplug',
            name='guid_tube_position',
            field=models.OneToOneField(to='tragopan.FuelAssemblyPosition'),
        ),
        migrations.AlterField(
            model_name='sourcerodmap',
            name='guid_tube_position',
            field=models.OneToOneField(to='tragopan.FuelAssemblyPosition'),
        ),
        migrations.DeleteModel(
            name='GuidTubeMap',
        ),
        migrations.DeleteModel(
            name='InstrumentTubePosition',
        ),
    ]
