# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0059_auto_20150728_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controlrodassembly',
            old_name='custer_name',
            new_name='cluster_name',
        ),
    ]
