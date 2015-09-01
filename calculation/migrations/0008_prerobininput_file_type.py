# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0007_auto_20150818_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='prerobininput',
            name='file_type',
            field=models.CharField(choices=[('BASE_FUEL', 'BASE_FUEL'), ('BP_OUT', 'BP_OUT'), ('BR', 'BR')], max_length=9, default='BASE_FUEL'),
            preserve_default=False,
        ),
    ]
