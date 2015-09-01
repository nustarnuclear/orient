# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0043_auto_20150728_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burnablepoisonassembly',
            name='fuel_assembly_model',
            field=models.ForeignKey(to='tragopan.FuelAssemblyModel'),
        ),
        migrations.AlterField(
            model_name='burnablepoisonrodmap',
            name='burnable_poison_position',
            field=models.ForeignKey(to='tragopan.FuelAssemblyPosition'),
        ),
        migrations.AlterUniqueTogether(
            name='burnablepoisonrodmap',
            unique_together=set([('burnable_poison_assembly', 'burnable_poison_position')]),
        ),
    ]
