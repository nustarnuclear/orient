# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0050_auto_20150728_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlrodassembly',
            name='primary',
            field=models.BooleanField(verbose_name='if primary?', default=False),
        ),
    ]
