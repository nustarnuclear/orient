# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0076_auto_20150817_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlrodmap',
            name='control_rod_assembly',
            field=models.ForeignKey(to='tragopan.ControlRodAssembly', related_name='control_rods'),
        ),
    ]
