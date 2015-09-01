# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0091_materialcomposition_element_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialcomposition',
            name='weight_percent',
            field=models.DecimalField(blank=True, max_digits=9, null=True, help_text='unit:%', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], decimal_places=6),
        ),
    ]
