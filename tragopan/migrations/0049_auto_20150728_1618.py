# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0048_auto_20150728_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlrodassembly',
            name='custer_name',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='controlrodassembly',
            name='type',
            field=models.CharField(default=1, max_length=8, choices=[('shutdown', 'shutdown'), ('adjust', 'adjust')]),
            preserve_default=False,
        ),
    ]
