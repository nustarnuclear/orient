# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0005_auto_20150812_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prerobinbranch',
            old_name='fuel_moderator_interval',
            new_name='moderator_temperature_interval',
        ),
    ]
