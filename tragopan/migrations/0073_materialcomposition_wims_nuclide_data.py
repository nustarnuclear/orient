# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0072_wimsnuclidedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialcomposition',
            name='wims_nuclide_data',
            field=models.ForeignKey(verbose_name='Related Lookup (FK)', null=True, to='tragopan.WimsNuclideData', blank=True),
        ),
    ]
