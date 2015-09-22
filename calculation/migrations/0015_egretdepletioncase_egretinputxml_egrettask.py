# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import calculation.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tragopan', '0100_auto_20150921_1143'),
        ('calculation', '0014_auto_20150921_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='EgretDepletionCase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ralative_power', models.DecimalField(max_digits=6, decimal_places=5, help_text='0-1.5', validators=[django.core.validators.MaxValueValidator(1.5), django.core.validators.MinValueValidator(0)])),
                ('burnup', models.DecimalField(max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], blank=True, null=True, help_text='GWd/tU')),
                ('bank_position', models.CommaSeparatedIntegerField(max_length=100)),
                ('delta_time', models.DecimalField(max_digits=10, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)], blank=True, null=True, help_text='day')),
                ('SDC', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'egret_depletion_case',
            },
        ),
        migrations.CreateModel(
            name='EgretInputXML',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('base_component_xml', models.FileField(upload_to=calculation.models.get_egret_base_component_xml_path)),
                ('base_core_xml', models.FileField(upload_to=calculation.models.get_egret_base_core_xml_path)),
                ('loading_pattern_xml', models.FileField(upload_to=calculation.models.get_egret_loading_pattern_xml_path)),
                ('unit', models.ForeignKey(to='tragopan.UnitParameter')),
            ],
            options={
                'db_table': 'egret_input_xml',
            },
        ),
        migrations.CreateModel(
            name='EgretTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('task_name', models.CharField(max_length=32)),
                ('egret_input_file', models.FileField(upload_to=calculation.models.get_egret_upload_path)),
                ('cycle', models.ForeignKey(to='tragopan.Cycle')),
                ('depletion_composition', models.ManyToManyField(to='calculation.EgretDepletionCase')),
                ('user', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'egret_task',
            },
        ),
    ]
