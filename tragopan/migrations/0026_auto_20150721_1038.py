# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0025_auto_20150721_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuelelementpelletloadingscheme',
            name='fuel_pellet',
        ),
        migrations.AddField(
            model_name='fuelelementpelletloadingscheme',
            name='fuel_pellet_type',
            field=models.ForeignKey(to='tragopan.FuelPelletType', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fuelelementtype',
            name='pellet',
            field=models.ManyToManyField(through='tragopan.FuelElementPelletLoadingScheme', to='tragopan.FuelPelletType'),
        ),
    ]
