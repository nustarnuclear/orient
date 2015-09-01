# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0068_auto_20150812_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelassemblytype',
            name='assembly_enrichment',
            field=models.DecimalField(help_text='meaningful only if using the one unique enrichment fuel', null=True, blank=True, validators=[django.core.validators.MinValueValidator(0)], decimal_places=4, max_digits=6),
        ),
    ]
