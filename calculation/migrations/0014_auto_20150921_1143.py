# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0100_auto_20150921_1143'),
        ('calculation', '0013_ibis_burnable_poison_assembly'),
    ]

    operations = [
        migrations.AddField(
            model_name='ibis',
            name='plant',
            field=models.ForeignKey(to='tragopan.Plant', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basefuelcomposition',
            name='ibis',
            field=models.ForeignKey(related_name='base_fuels', to='calculation.Ibis'),
        ),
    ]
