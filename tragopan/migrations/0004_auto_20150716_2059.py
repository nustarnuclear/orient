# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0003_auto_20150716_2054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nuclide',
            options={'ordering': ['atom_mass']},
        ),
    ]
