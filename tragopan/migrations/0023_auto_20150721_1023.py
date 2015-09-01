# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0022_auto_20150721_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelAssemblyType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'fuel_assembly_type',
            },
        ),
        migrations.CreateModel(
            name='FuelElementType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model', models.ForeignKey(to='tragopan.FuelElement')),
            ],
            options={
                'db_table': 'fuel_element_type',
            },
        ),
        migrations.CreateModel(
            name='FuelElementTypePosition',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('fuel_assembly_position', models.ForeignKey(to='tragopan.FuelAssemblyPosition')),
                ('fuel_assembly_type', models.ForeignKey(to='tragopan.FuelAssemblyType')),
                ('fuel_element_type', models.ForeignKey(to='tragopan.FuelElementType')),
            ],
            options={
                'db_table': 'fuel_element_type_position',
            },
        ),
        migrations.RemoveField(
            model_name='fuelelementpelletloadingscheme',
            name='order',
        ),
        migrations.AddField(
            model_name='fuelelementpelletloadingscheme',
            name='section',
            field=models.DecimalField(max_digits=7, help_text='unit:cm height base on bottom', default=0, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fuelelementpelletloadingscheme',
            name='fuel_element_type',
            field=models.ForeignKey(to='tragopan.FuelElementType'),
        ),
        migrations.AddField(
            model_name='fuelelementtype',
            name='pellet',
            field=models.ManyToManyField(to='tragopan.FuelPelletType', through='tragopan.FuelElementPelletLoadingScheme'),
        ),
        migrations.AddField(
            model_name='fuelassemblytype',
            name='fuel_element_Type_position',
            field=models.ManyToManyField(to='tragopan.FuelElementType', through='tragopan.FuelElementTypePosition'),
        ),
        migrations.AddField(
            model_name='fuelassemblytype',
            name='model',
            field=models.ForeignKey(to='tragopan.FuelAssemblyModel'),
        ),
    ]
