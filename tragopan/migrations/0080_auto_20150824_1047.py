# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0079_auto_20150824_1027'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fuelassemblyloadingpattern',
            unique_together=set([('cycle', 'fuel_assembly'), ('cycle', 'reactor_position')]),
        ),
    ]
