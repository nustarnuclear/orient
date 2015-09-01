# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0087_auto_20150825_1431'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='materialcomposition',
            unique_together=set([]),
        ),
    ]
