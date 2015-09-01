# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0010_auto_20150720_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelassemblyrepository',
            name='PN',
            field=models.CharField(unique=True, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fuelassemblyrepository',
            name='arrival_date',
            field=models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fuelassemblyrepository',
            name='batch_number',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fuelassemblyrepository',
            name='manufacturing_date',
            field=models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date', null=True, blank=True),
        ),
    ]
