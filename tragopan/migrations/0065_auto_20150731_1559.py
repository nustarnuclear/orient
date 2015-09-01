# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0064_burnablepoisonrodmap_insert_depth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='burnablepoisonrodmap',
            old_name='insert_depth',
            new_name='height',
        ),
    ]
