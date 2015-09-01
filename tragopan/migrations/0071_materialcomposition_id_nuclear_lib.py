# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0070_auto_20150812_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialcomposition',
            name='id_nuclear_lib',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
