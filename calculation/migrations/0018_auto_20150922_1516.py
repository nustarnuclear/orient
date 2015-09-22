# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import calculation.models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0017_auto_20150922_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egrettask',
            name='egret_input_file',
            field=models.FileField(blank=True, null=True, upload_to=calculation.models.get_egret_upload_path),
        ),
        migrations.AlterField(
            model_name='egrettask',
            name='restart_file',
            field=models.FilePathField(blank=True, null=True, recursive=True, path='C:\\Users\\zh\\git\\tragopan\\media'),
        ),
    ]
