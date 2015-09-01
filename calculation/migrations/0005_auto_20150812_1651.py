# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0004_prerobininput_use_pre_segment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prerobininput',
            name='branch_composition',
            field=models.ManyToManyField(related_name='branches', to='calculation.PreRobinBranch'),
        ),
    ]
