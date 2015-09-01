# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0074_auto_20150817_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialcomposition',
            name='element',
            field=models.ForeignKey(blank=True, null=True, to='tragopan.Element'),
        ),
    ]
