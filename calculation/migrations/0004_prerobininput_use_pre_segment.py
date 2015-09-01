# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0003_auto_20150812_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='prerobininput',
            name='use_pre_segment',
            field=models.ForeignKey(blank=True, null=True, to='calculation.PreRobinInput'),
        ),
    ]
