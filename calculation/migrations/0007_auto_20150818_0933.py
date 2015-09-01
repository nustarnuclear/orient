# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import calculation.models


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0077_auto_20150818_0933'),
        ('calculation', '0006_auto_20150814_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='prerobininput',
            name='plant',
            field=models.ForeignKey(to='tragopan.Plant', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prerobininput',
            name='pre_robin_file',
            field=models.FileField(null=True, upload_to=calculation.models.get_pre_robin_upload_path, blank=True),
        ),
    ]
