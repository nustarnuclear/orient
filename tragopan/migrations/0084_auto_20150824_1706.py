# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0083_auto_20150824_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='WmisElementComposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight_percent', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', decimal_places=6, max_digits=9)),
            ],
            options={
                'db_table': 'wmis_element_composition',
            },
        ),
        migrations.CreateModel(
            name='WmisElementData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('element_name', models.CharField(max_length=30)),
                ('composition', models.ManyToManyField(to='tragopan.WimsNuclideData', through='tragopan.WmisElementComposition')),
            ],
            options={
                'db_table': 'wmis_element_data',
            },
        ),
        migrations.AddField(
            model_name='wmiselementcomposition',
            name='wmis_element',
            field=models.ForeignKey(to='tragopan.WmisElementData'),
        ),
        migrations.AddField(
            model_name='wmiselementcomposition',
            name='wmis_nuclide',
            field=models.ForeignKey(to='tragopan.WimsNuclideData'),
        ),
    ]
