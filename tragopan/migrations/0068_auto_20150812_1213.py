# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0067_material_prerobin_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelassemblytype',
            name='assembly_enrichment',
            field=models.DecimalField(max_digits=6, blank=True, help_text='meaningful only if using the one unique enrichment fuel', decimal_places=5, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='material',
            name='prerobin_identifier',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
