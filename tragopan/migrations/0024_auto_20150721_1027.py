# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0023_auto_20150721_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelPellet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(decimal_places=3, blank=True, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm can be none when hollow', null=True)),
                ('length', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('dish_volume_percentage', models.DecimalField(decimal_places=6, blank=True, max_digits=9, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', null=True)),
                ('chamfer_volume_percentage', models.DecimalField(decimal_places=6, blank=True, max_digits=9, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', null=True)),
                ('dish_depth', models.DecimalField(decimal_places=3, blank=True, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', null=True)),
                ('dish_diameter', models.DecimalField(decimal_places=3, blank=True, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', null=True)),
                ('roughness', models.DecimalField(decimal_places=6, blank=True, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', null=True)),
                ('nominal_density', models.DecimalField(help_text='unit:g/cm3', decimal_places=5, max_digits=8, validators=[django.core.validators.MinValueValidator(0)])),
                ('uncertainty_percentage', models.DecimalField(decimal_places=6, blank=True, max_digits=9, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', null=True)),
                ('coating_thickness', models.DecimalField(decimal_places=3, blank=True, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', null=True)),
                ('coating_material', models.ForeignKey(to='tragopan.Material', blank=True, null=True, related_name='fuel_pellet_coating')),
                ('fuel_assembly_model', models.OneToOneField(to='tragopan.FuelAssemblyModel')),
                ('material', models.ForeignKey(to='tragopan.Material', related_name='fuel_pellet_material')),
            ],
            options={
                'db_table': 'fuel_pellet',
            },
        ),
        migrations.RemoveField(
            model_name='fuelpellettype',
            name='coating_material',
        ),
        migrations.RemoveField(
            model_name='fuelpellettype',
            name='fuel_assembly_model',
        ),
        migrations.RemoveField(
            model_name='fuelpellettype',
            name='material',
        ),
        migrations.RemoveField(
            model_name='fuelelementpelletloadingscheme',
            name='fuel_pellet_type',
        ),
        migrations.AlterField(
            model_name='fuelelementtype',
            name='pellet',
            field=models.ManyToManyField(through='tragopan.FuelElementPelletLoadingScheme', to='tragopan.FuelPellet'),
        ),
        migrations.DeleteModel(
            name='FuelPelletType',
        ),
        migrations.AddField(
            model_name='fuelelementpelletloadingscheme',
            name='fuel_pellet',
            field=models.ForeignKey(default=1, to='tragopan.FuelPellet'),
            preserve_default=False,
        ),
    ]
