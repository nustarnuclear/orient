# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0039_auto_20150724_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactormodel',
            name='cold_state_assembly_pitch',
            field=models.DecimalField(help_text='unit:cm', validators=[django.core.validators.MinValueValidator(0)], null=True, blank=True, decimal_places=4, max_digits=7),
        ),
        migrations.AlterField(
            model_name='reactormodel',
            name='hot_state_assembly_pitch',
            field=models.DecimalField(help_text='unit:cm', validators=[django.core.validators.MinValueValidator(0)], null=True, blank=True, decimal_places=4, max_digits=7),
        ),
    ]
