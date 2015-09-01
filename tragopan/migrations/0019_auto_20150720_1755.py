# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0018_auto_20150720_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuelelementtype',
            name='fuel_pellet',
        ),
        migrations.AddField(
            model_name='fakefuelelementtype',
            name='fuel_assembly_model',
            field=models.OneToOneField(default=1, to='tragopan.FuelAssemblyModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuelelementtype',
            name='fuel_assembly_model',
            field=models.OneToOneField(default=1, to='tragopan.FuelAssemblyModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuelpellettype',
            name='fuel_assembly_model',
            field=models.OneToOneField(default=1, to='tragopan.FuelAssemblyModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guidtube',
            name='fuel_assembly_model',
            field=models.OneToOneField(default=1, to='tragopan.FuelAssemblyModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instrumenttube',
            name='fuel_assembly_model',
            field=models.OneToOneField(default=1, to='tragopan.FuelAssemblyModel'),
            preserve_default=False,
        ),
    ]
