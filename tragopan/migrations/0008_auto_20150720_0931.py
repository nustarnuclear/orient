# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0007_auto_20150716_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelassemblyrepository',
            name='arrival_date',
            field=models.DateField(null=True, help_text='Please use <b>YYYY-MM-DD<b> to input the date'),
        ),
        migrations.AlterField(
            model_name='fuelassemblyrepository',
            name='manufacturing_date',
            field=models.DateField(null=True, help_text='Please use <b>YYYY-MM-DD<b> to input the date'),
        ),
    ]
