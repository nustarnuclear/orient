# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0033_auto_20150721_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelassemblyrepository',
            name='vendor',
            field=models.ForeignKey(default=1, to='tragopan.Vendor'),
        ),
    ]
