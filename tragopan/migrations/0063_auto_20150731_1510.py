# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0062_auto_20150729_1410'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='controlrodassemblyloadingpattern',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='controlrodassemblyloadingpattern',
            name='cycle',
        ),
    ]
