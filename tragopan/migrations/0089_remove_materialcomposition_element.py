# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0088_auto_20150825_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialcomposition',
            name='element',
        ),
    ]
