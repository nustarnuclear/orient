# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0061_auto_20150729_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controlrodmap',
            old_name='guid_tube_position',
            new_name='guide_tube_position',
        ),
        migrations.AlterUniqueTogether(
            name='controlrodmap',
            unique_together=set([('control_rod_assembly', 'guide_tube_position')]),
        ),
    ]
