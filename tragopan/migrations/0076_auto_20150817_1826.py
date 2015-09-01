# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0075_auto_20150817_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fuelelement',
            old_name='filling_gas_materia',
            new_name='filling_gas_material',
        ),
    ]
