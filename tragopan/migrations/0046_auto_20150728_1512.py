# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0045_auto_20150728_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reactormodel',
            name='num_control_rod_mechanisms',
        ),
        migrations.AddField(
            model_name='reactorposition',
            name='control_rod_mechanism',
            field=models.BooleanField(default=False, help_text='whether contain control rod mechanism'),
        ),
    ]
