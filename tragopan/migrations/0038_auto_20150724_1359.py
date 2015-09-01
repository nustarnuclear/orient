# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0037_auto_20150721_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reactormodel',
            name='model',
        ),
        migrations.AddField(
            model_name='reactormodel',
            name='name',
            field=models.CharField(max_length=50, default='QNPC2'),
            preserve_default=False,
        ),
    ]
