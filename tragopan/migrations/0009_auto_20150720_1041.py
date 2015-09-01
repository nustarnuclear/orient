# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0008_auto_20150720_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cycle',
            name='num_periodical_tests',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cycle',
            name='num_unplanned_shutdowns',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
