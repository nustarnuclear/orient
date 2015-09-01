# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0029_auto_20150721_1305'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fuelelementtypeposition',
            unique_together=set([('fuel_assembly_type', 'fuel_assembly_position')]),
        ),
    ]
