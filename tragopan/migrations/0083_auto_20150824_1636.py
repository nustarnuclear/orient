# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0082_auto_20150824_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wimsnuclidedata',
            name='id_self_defined',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
