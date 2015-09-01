# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0016_auto_20150720_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fuelpellettype',
            old_name='dish_height',
            new_name='length',
        ),
        migrations.RemoveField(
            model_name='fuelpellettype',
            name='density_percentage',
        ),
        migrations.RemoveField(
            model_name='fuelpellettype',
            name='height',
        ),
        migrations.AddField(
            model_name='fuelpellettype',
            name='chamfer_volume_percentage',
            field=models.DecimalField(help_text='unit:%', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], null=True, max_digits=9, decimal_places=6, blank=True),
        ),
        migrations.AddField(
            model_name='fuelpellettype',
            name='dish_depth',
            field=models.DecimalField(help_text='unit:cm', validators=[django.core.validators.MinValueValidator(0)], null=True, max_digits=7, decimal_places=3, blank=True),
        ),
        migrations.AddField(
            model_name='fuelpellettype',
            name='nominal_density',
            field=models.DecimalField(max_digits=8, decimal_places=5, help_text='unit:g/cm3', default=10.41, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fuelpellettype',
            name='coating_material',
            field=models.ForeignKey(related_name='fuel_pellet_coating', null=True, blank=True, to='tragopan.Material'),
        ),
        migrations.AlterField(
            model_name='fuelpellettype',
            name='coating_thickness',
            field=models.DecimalField(help_text='unit:cm', validators=[django.core.validators.MinValueValidator(0)], null=True, max_digits=7, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='fuelpellettype',
            name='dish_diameter',
            field=models.DecimalField(help_text='unit:cm', validators=[django.core.validators.MinValueValidator(0)], null=True, max_digits=7, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='fuelpellettype',
            name='dish_volume_percentage',
            field=models.DecimalField(help_text='unit:%', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], null=True, max_digits=9, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='fuelpellettype',
            name='uncertainty_percentage',
            field=models.DecimalField(help_text='unit:%', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], null=True, max_digits=9, decimal_places=6, blank=True),
        ),
    ]
