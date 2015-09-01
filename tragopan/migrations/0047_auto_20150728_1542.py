# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0046_auto_20150728_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlrodmap',
            name='guid_tube_position',
            field=models.ForeignKey(to='tragopan.FuelAssemblyPosition'),
        ),
        migrations.AlterField(
            model_name='reactorposition',
            name='control_rod_mechanism',
            field=models.BooleanField(help_text='whether contain control rod mechanism', verbose_name='Whether can be inserted control rod assembly?', default=False),
        ),
        migrations.AlterUniqueTogether(
            name='controlrodmap',
            unique_together=set([('control_rod_assembly', 'guid_tube_position')]),
        ),
    ]
