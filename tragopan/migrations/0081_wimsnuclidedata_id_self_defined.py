# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0080_auto_20150824_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='wimsnuclidedata',
            name='id_self_defined',
            field=models.PositiveSmallIntegerField(blank=True, null=True, unique=True),
        ),
    ]
