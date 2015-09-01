# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0027_auto_20150721_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelassemblyposition',
            name='type',
            field=models.CharField(max_length=10, default='fuel', choices=[('fuel', 'fuel element tube'), ('guide', 'guide tube'), ('instrument', 'instrument tube')]),
        ),
        migrations.AlterField(
            model_name='fuelelementtypeposition',
            name='fuel_assembly_type',
            field=models.ForeignKey(related_name='positions', related_query_name='position', to='tragopan.FuelAssemblyType'),
        ),
    ]
