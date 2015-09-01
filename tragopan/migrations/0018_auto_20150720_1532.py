# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0017_auto_20150720_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelassemblyloadingpattern',
            name='dragable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fuelassemblyloadingpattern',
            name='following_index',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
    ]
