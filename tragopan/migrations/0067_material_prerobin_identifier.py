# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0066_auto_20150807_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='prerobin_identifier',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
