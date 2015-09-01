# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0094_auto_20150826_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='atomic_number',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
    ]
