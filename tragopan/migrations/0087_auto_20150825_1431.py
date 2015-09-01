# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0086_remove_materialcomposition_wims_nuclide_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='material_composition',
            field=models.ManyToManyField(through='tragopan.MaterialComposition', to='tragopan.WmisElementData'),
        ),
    ]
