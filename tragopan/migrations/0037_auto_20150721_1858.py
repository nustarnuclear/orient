# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0036_auto_20150721_1848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reactorposition',
            options={'ordering': ['row', 'column']},
        ),
    ]
