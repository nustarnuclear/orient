# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0009_auto_20150914_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basefuelcomposition',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='basefuelcomposition',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='basefuelcomposition',
            name='time_inserted',
        ),
        migrations.RemoveField(
            model_name='basefuelcomposition',
            name='user',
        ),
    ]
