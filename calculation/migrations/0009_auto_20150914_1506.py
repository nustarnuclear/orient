# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0097_auto_20150914_1440'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calculation', '0008_prerobininput_file_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseFuel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('fuel_identity', models.CharField(max_length=32)),
                ('offset', models.BooleanField(default=False)),
                ('base_bottom', models.DecimalField(decimal_places=5, default=0, validators=[django.core.validators.MinValueValidator(0)], help_text='cm', max_digits=10)),
            ],
            options={
                'db_table': 'base_fuel',
            },
        ),
        migrations.CreateModel(
            name='BaseFuelComposition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(decimal_places=5, default=0, validators=[django.core.validators.MinValueValidator(0)], help_text='cm', max_digits=10)),
                ('base_fuel', models.ForeignKey(to='calculation.BaseFuel')),
            ],
            options={
                'db_table': 'base_fuel_composition',
            },
        ),
        migrations.AddField(
            model_name='ibis',
            name='fuel_assembly_type',
            field=models.ForeignKey(default=1, to='tragopan.FuelAssemblyType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ibis',
            name='ibis_name',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basefuelcomposition',
            name='ibis',
            field=models.ForeignKey(to='calculation.Ibis'),
        ),
        migrations.AddField(
            model_name='basefuelcomposition',
            name='user',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='basefuel',
            name='axial_composition',
            field=models.ManyToManyField(through='calculation.BaseFuelComposition', to='calculation.Ibis'),
        ),
        migrations.AddField(
            model_name='basefuel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
