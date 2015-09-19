# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0098_auto_20150919_1351'),
        ('calculation', '0012_auto_20150918_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='ibis',
            name='burnable_poison_assembly',
            field=models.ForeignKey(blank=True, to='tragopan.BurnablePoisonAssembly', null=True),
        ),
    ]
