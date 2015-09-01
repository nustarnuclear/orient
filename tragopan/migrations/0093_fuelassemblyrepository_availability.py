# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0092_auto_20150825_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelassemblyrepository',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]
