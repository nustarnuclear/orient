# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0063_auto_20150731_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='burnablepoisonrodmap',
            name='insert_depth',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, default=7.4575, help_text='unit:cm', max_digits=7),
            preserve_default=False,
        ),
    ]
