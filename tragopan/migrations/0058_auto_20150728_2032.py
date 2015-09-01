# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0057_auto_20150728_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='grid',
            name='name',
            field=models.CharField(max_length=50, default='端部格架'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grid',
            name='sleeve_height',
            field=models.DecimalField(help_text='cm', decimal_places=5, validators=[django.core.validators.MinValueValidator(0)], max_digits=15),
        ),
    ]
