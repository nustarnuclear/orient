# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0020_auto_20150720_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuelassemblymodel',
            name='model',
        ),
        migrations.AddField(
            model_name='fuelassemblymodel',
            name='name',
            field=models.CharField(default='AFA2G', max_length=20),
            preserve_default=False,
        ),
    ]
