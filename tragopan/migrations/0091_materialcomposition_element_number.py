# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0090_auto_20150825_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialcomposition',
            name='element_number',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
