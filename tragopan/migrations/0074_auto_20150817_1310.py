# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0073_materialcomposition_wims_nuclide_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialcomposition',
            name='id_nuclear_lib',
        ),
        migrations.AlterField(
            model_name='fuelassemblyloadingpattern',
            name='cycle',
            field=models.ForeignKey(related_name='cycles', to='tragopan.Cycle'),
        ),
        migrations.AlterField(
            model_name='fuelassemblyloadingpattern',
            name='fuel_assembly',
            field=models.ForeignKey(default=1, related_name='cycle_positions', to='tragopan.FuelAssemblyRepository'),
        ),
        migrations.AlterField(
            model_name='materialcomposition',
            name='wims_nuclide_data',
            field=models.ForeignKey(blank=True, null=True, to='tragopan.WimsNuclideData'),
        ),
    ]
