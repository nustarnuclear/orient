# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0081_wimsnuclidedata_id_self_defined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wimsnuclidedata',
            name='id_wims',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
