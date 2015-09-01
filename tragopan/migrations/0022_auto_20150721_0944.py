# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0021_auto_20150721_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelElement',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('overall_length', models.DecimalField(help_text='unit:cm', max_digits=7, validators=[django.core.validators.MinValueValidator(0)], decimal_places=3)),
                ('active_length', models.DecimalField(help_text='unit:cm', max_digits=7, validators=[django.core.validators.MinValueValidator(0)], decimal_places=3)),
                ('plenum_length', models.DecimalField(help_text='unit:cm', max_digits=7, validators=[django.core.validators.MinValueValidator(0)], decimal_places=3)),
                ('filling_gas_pressure', models.DecimalField(help_text='unit:MPa', max_digits=10, validators=[django.core.validators.MinValueValidator(0)], decimal_places=5)),
                ('filling_gas_materia', models.ForeignKey(to='tragopan.Material')),
                ('fuel_assembly_model', models.OneToOneField(to='tragopan.FuelAssemblyModel')),
                ('vendor', models.ForeignKey(to='tragopan.Vendor')),
            ],
            options={
                'db_table': 'fuel_element',
            },
        ),
        migrations.RemoveField(
            model_name='fuelelementtype',
            name='filling_gas_materia',
        ),
        migrations.RemoveField(
            model_name='fuelelementtype',
            name='fuel_assembly_model',
        ),
        migrations.RemoveField(
            model_name='fuelelementtype',
            name='vendor',
        ),
        migrations.AlterField(
            model_name='claddingtube',
            name='fuel_element_type',
            field=models.OneToOneField(to='tragopan.FuelElement'),
        ),
        migrations.AlterField(
            model_name='fuelelementpelletloadingscheme',
            name='fuel_element_type',
            field=models.ForeignKey(to='tragopan.FuelElement'),
        ),
        migrations.AlterField(
            model_name='lowercap',
            name='fuel_element_type',
            field=models.OneToOneField(to='tragopan.FuelElement'),
        ),
        migrations.AlterField(
            model_name='plenumspring',
            name='fuel_element_type',
            field=models.OneToOneField(to='tragopan.FuelElement'),
        ),
        migrations.AlterField(
            model_name='uppercap',
            name='fuel_element_type',
            field=models.OneToOneField(to='tragopan.FuelElement'),
        ),
        migrations.DeleteModel(
            name='FuelElementType',
        ),
    ]
