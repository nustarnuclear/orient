# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0066_auto_20150807_1932'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PreRobinBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('identity', models.CharField(max_length=32)),
                ('max_boron_density', models.PositiveSmallIntegerField(blank=True, null=True, help_text='ppm')),
                ('min_boron_density', models.PositiveSmallIntegerField(blank=True, null=True, help_text='ppm', default=0)),
                ('boron_density_interval', models.PositiveSmallIntegerField(blank=True, null=True, help_text='ppm', default=200)),
                ('max_fuel_temperature', models.PositiveSmallIntegerField(blank=True, null=True, help_text='K')),
                ('min_fuel_temperature', models.PositiveSmallIntegerField(blank=True, null=True, help_text='K')),
                ('fuel_temperature_interval', models.PositiveSmallIntegerField(blank=True, null=True, help_text='K', default=50)),
                ('max_moderator_temperature', models.PositiveSmallIntegerField(blank=True, null=True, help_text='K')),
                ('min_moderator_temperature', models.PositiveSmallIntegerField(blank=True, null=True, help_text='K')),
                ('fuel_moderator_interval', models.PositiveSmallIntegerField(blank=True, null=True, help_text='K', default=4)),
                ('shutdown_cooling_days', models.PositiveSmallIntegerField(blank=True, null=True, help_text='day')),
                ('xenon', models.BooleanField(default=False, verbose_name='set xenon density to 0?')),
                ('control_rod_assembly', models.ForeignKey(blank=True, null=True, to='tragopan.ControlRodAssembly')),
            ],
            options={
                'db_table': 'pre_robin_branch',
            },
        ),
        migrations.CreateModel(
            name='PreRobinInput',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('segment_identity', models.CharField(max_length=32)),
                ('power_density', models.DecimalField(blank=True, validators=[django.core.validators.MinValueValidator(0)], null=True, max_digits=10, help_text='w/g', decimal_places=5)),
                ('assembly_maxium_burnup', models.DecimalField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], null=True, max_digits=7, help_text='GWd/tU', decimal_places=5)),
                ('boron_density', models.DecimalField(blank=True, validators=[django.core.validators.MinValueValidator(0)], null=True, max_digits=10, help_text='ppm', decimal_places=5)),
                ('moderator_temperature', models.DecimalField(blank=True, validators=[django.core.validators.MinValueValidator(0)], null=True, max_digits=10, help_text='K', decimal_places=5)),
                ('fuel_temperature', models.DecimalField(blank=True, validators=[django.core.validators.MinValueValidator(0)], null=True, max_digits=10, help_text='K', decimal_places=5)),
                ('num_fuel_assembly', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 1), (2, 2), (3, 3)])),
                ('num_edit_node', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(16, 16), (4, 4)], default=16)),
                ('branch_composition', models.ManyToManyField(to='calculation.PreRobinBranch')),
                ('burnable_poison_assembly', models.ForeignKey(blank=True, null=True, to='tragopan.BurnablePoisonAssembly')),
                ('core_baffle', models.ForeignKey(blank=True, null=True, to='tragopan.CoreBaffle')),
                ('fuel_assembly_type', models.ForeignKey(to='tragopan.FuelAssemblyType')),
                ('grid', models.ForeignKey(blank=True, null=True, to='tragopan.Grid')),
            ],
            options={
                'db_table': 'pre_robin_input',
            },
        ),
        migrations.CreateModel(
            name='PreRobinModel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model_name', models.CharField(max_length=32)),
                ('system_pressure', models.DecimalField(default=15.51, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, help_text='MPa')),
                ('dep_strategy', models.CharField(blank=True, null=True, choices=[('LLR', 'LLR'), ('PPC', 'PPC'), ('LR', 'LR'), ('PC', 'PC')], default='LLR', max_length=3)),
                ('track_density', models.DecimalField(default=0.03, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, help_text='cm')),
                ('polar_type', models.CharField(max_length=4, choices=[('LCMD', 'LCMD'), ('TYPL', 'TYPL'), ('DeCT', 'DeCT')], default='LCMD')),
                ('polar_azimuth', models.CommaSeparatedIntegerField(max_length=50, default='4,16')),
                ('iter_inner', models.PositiveSmallIntegerField(default=3)),
                ('iter_outer', models.PositiveSmallIntegerField(default=100)),
                ('eps_keff', models.DecimalField(default=1e-05, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], decimal_places=5)),
                ('eps_flux', models.DecimalField(default=0.0001, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], decimal_places=5)),
                ('leakage_corrector_path', models.PositiveSmallIntegerField(default=2, choices=[(0, 0), (1, 1), (2, 2)])),
                ('leakage_corrector_method', models.CharField(max_length=2, choices=[('B1', 'B1'), ('P1', 'P1')], default='B1')),
                ('buckling_or_keff', models.DecimalField(default=1, max_digits=10, decimal_places=5)),
                ('condensation_path', models.PositiveSmallIntegerField(default=1, choices=[(0, 0), (1, 1), (2, 2)])),
                ('num_group_2D', models.PositiveSmallIntegerField(default=25, choices=[(2, 2), (3, 3), (4, 4), (8, 8), (18, 18), (25, 25), (33, 33)])),
                ('num_group_edit', models.PositiveSmallIntegerField(default=2, choices=[(2, 2), (3, 3), (4, 4), (8, 8), (18, 18), (25, 25), (33, 33)])),
                ('micro_xs_output', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pre_robin_model',
            },
        ),
        migrations.AddField(
            model_name='prerobininput',
            name='pre_robin_model',
            field=models.ForeignKey(default=1, to='calculation.PreRobinModel'),
        ),
        migrations.AddField(
            model_name='prerobininput',
            name='user',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
