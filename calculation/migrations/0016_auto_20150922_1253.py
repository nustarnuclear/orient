# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0015_egretdepletioncase_egretinputxml_egrettask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='egrettask',
            name='depletion_composition',
        ),
        migrations.DeleteModel(
            name='EgretDepletionCase',
        ),
    ]
