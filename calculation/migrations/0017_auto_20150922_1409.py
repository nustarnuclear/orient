# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0016_auto_20150922_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='egrettask',
            name='follow_index',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='egrettask',
            name='restart_file',
            field=models.FilePathField(blank=True, null=True, path='c:'),
        ),
    ]
