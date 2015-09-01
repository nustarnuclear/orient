# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0069_auto_20150812_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelassemblytype',
            name='assembly_enrichment',
            field=models.DecimalField(help_text='meaningful only if using the one unique enrichment fuel', validators=[django.core.validators.MinValueValidator(0)], blank=True, decimal_places=3, null=True, max_digits=4),
        ),
    ]
