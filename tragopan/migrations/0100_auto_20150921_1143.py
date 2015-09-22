# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0099_reactormodel_fuel_pitch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactormodel',
            name='name',
            field=models.CharField(choices=[('CP600', 'CP600'), ('CP300', 'CP300'), ('M310', 'M310'), ('CAP1000', 'CAP1000'), ('AP1000', 'AP1000')], max_length=50),
        ),
    ]
