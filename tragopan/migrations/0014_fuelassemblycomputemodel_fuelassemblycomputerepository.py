# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0013_remove_fuelassemblymodel_fuel_enrichment'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelAssemblyComputeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model', models.CharField(choices=[('AFA2G', 'AFA2G'), ('AFA3G', 'AFA3G')], max_length=5)),
                ('fuel_enrichment', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], max_digits=9, help_text='unit:% U235', decimal_places=6)),
            ],
            options={
                'db_table': 'fuel_assembly_model_compute',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyComputeRepository',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model', models.ForeignKey(to='tragopan.FuelAssemblyModel')),
                ('plant', models.ForeignKey(to='tragopan.Plant')),
            ],
            options={
                'db_table': 'fuel_assembly_repository_compute',
            },
        ),
    ]
