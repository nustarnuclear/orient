# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0030_auto_20150721_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelelementpelletloadingscheme',
            name='fuel_element_type',
            field=models.ForeignKey(to='tragopan.FuelElementType', related_name='fuel_pellet_map'),
        ),
        migrations.AlterField(
            model_name='fuelpellet',
            name='dish_depth',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], blank=True, null=True, max_digits=7, help_text='unit:cm', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fuelpellet',
            name='dish_diameter',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], blank=True, null=True, max_digits=7, help_text='unit:cm', decimal_places=5),
        ),
    ]
