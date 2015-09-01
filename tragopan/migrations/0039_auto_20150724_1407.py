# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0038_auto_20150724_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactormodel',
            name='num_control_rod_mechanisms',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reactormodel',
            name='num_loops',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
