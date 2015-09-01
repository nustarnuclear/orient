# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0065_auto_20150731_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claddingtube',
            old_name='fuel_element_type',
            new_name='fuel_element',
        ),
        migrations.RenameField(
            model_name='lowercap',
            old_name='fuel_element_type',
            new_name='fuel_element',
        ),
        migrations.RenameField(
            model_name='plenumspring',
            old_name='fuel_element_type',
            new_name='fuel_element',
        ),
    ]
