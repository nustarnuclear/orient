# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0054_auto_20150728_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sourcerodmap',
            old_name='guid_tube_position',
            new_name='source_rod_position',
        ),
    ]
