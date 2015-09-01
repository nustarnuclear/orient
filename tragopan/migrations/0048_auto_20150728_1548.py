# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0047_auto_20150728_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlrodtype',
            name='absorb_diameter',
            field=models.DecimalField(max_digits=7, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='controlrodtype',
            name='absorb_length',
            field=models.DecimalField(max_digits=9, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='controlrodtype',
            name='cladding_inner_diameter',
            field=models.DecimalField(max_digits=7, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='controlrodtype',
            name='cladding_outer_diameter',
            field=models.DecimalField(max_digits=7, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', decimal_places=5),
        ),
    ]
