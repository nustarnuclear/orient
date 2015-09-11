# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0095_auto_20150828_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlRodAssemblyStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('step', models.PositiveSmallIntegerField()),
                ('control_rod_assembly', models.ForeignKey(to='tragopan.ControlRodAssembly')),
            ],
            options={
                'db_table': 'control_rod_assembly_step',
            },
        ),
        migrations.CreateModel(
            name='OperationParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('date', models.DateField(null=True, blank=True, help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('burnup', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, max_digits=15, help_text='unit:MWd/tU')),
                ('nuclear_power', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, max_digits=10, help_text='unit:MW')),
                ('theoretical_boron_density', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, max_digits=7, help_text='unit:ppm')),
                ('measured_boron_density', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, max_digits=7, help_text='unit:ppm')),
                ('coolant_average_temperature', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, max_digits=15, help_text='unit:K')),
                ('axial_power_shift', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(-100)], decimal_places=6, max_digits=9, help_text='unit:%FP')),
                ('control_rod_step', models.ManyToManyField(through='tragopan.ControlRodAssemblyStep', to='tragopan.ControlRodAssembly')),
                ('unit', models.ForeignKey(to='tragopan.UnitParameter')),
            ],
            options={
                'db_table': 'operation_parameter',
            },
        ),
        migrations.AddField(
            model_name='controlrodassemblystep',
            name='operation',
            field=models.ForeignKey(to='tragopan.OperationParameter'),
        ),
    ]
