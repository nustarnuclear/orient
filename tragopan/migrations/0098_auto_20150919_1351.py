# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0097_auto_20150914_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlrodassemblyloadingpattern',
            name='cycle',
            field=models.ForeignKey(to='tragopan.Cycle', related_name='control_rod_assembly_loading_patterns', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='controlrodassemblyloadingpattern',
            name='reactor_position',
            field=models.ForeignKey(to='tragopan.ReactorPosition', related_name='control_rod_assembly_pattern'),
        ),
        migrations.AlterField(
            model_name='cycle',
            name='unit',
            field=models.ForeignKey(to='tragopan.UnitParameter', related_name='cycles'),
        ),
        migrations.AlterField(
            model_name='fuelelement',
            name='fuel_assembly_model',
            field=models.OneToOneField(related_name='fuel_elements', to='tragopan.FuelAssemblyModel'),
        ),
        migrations.AlterField(
            model_name='reactormodel',
            name='name',
            field=models.CharField(max_length=50, choices=[('QNPC2', 'QNPC2'), ('QNPC1', 'QNPC1'), ('M310', 'M310'), ('CAP1000', 'CAP1000'), ('AP1000', 'AP1000')]),
        ),
    ]
