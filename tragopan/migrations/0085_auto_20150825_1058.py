# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0084_auto_20150824_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialnuclide',
            name='material',
        ),
        migrations.RemoveField(
            model_name='materialnuclide',
            name='nuclide',
        ),
        migrations.AddField(
            model_name='materialcomposition',
            name='wims_element_data',
            field=models.ForeignKey(null=True, blank=True, to='tragopan.WmisElementData'),
        ),
        migrations.AlterField(
            model_name='wmiselementcomposition',
            name='wmis_element',
            field=models.ForeignKey(to='tragopan.WmisElementData', related_name='nuclides'),
        ),
        migrations.DeleteModel(
            name='MaterialNuclide',
        ),
    ]
