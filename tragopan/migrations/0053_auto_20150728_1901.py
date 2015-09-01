# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0052_auto_20150728_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcerodtype',
            name='diameter',
            field=models.DecimalField(null=True, decimal_places=3, help_text='unit:cm', max_digits=7, blank=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='sourcerodtype',
            name='material',
            field=models.ForeignKey(to='tragopan.Material', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sourcerodtype',
            name='overall_length',
            field=models.DecimalField(null=True, decimal_places=3, help_text='unit:cm', max_digits=7, blank=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='sourcerodtype',
            name='strength',
            field=models.DecimalField(help_text='unit:10e8', max_digits=7, validators=[django.core.validators.MinValueValidator(0)], decimal_places=3),
        ),
    ]
