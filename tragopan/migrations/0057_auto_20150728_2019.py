# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0056_auto_20150728_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grid',
            name='model',
        ),
        migrations.RemoveField(
            model_name='grid',
            name='sleeve_thickness',
        ),
        migrations.RemoveField(
            model_name='grid',
            name='sleeve_weight',
        ),
        migrations.RemoveField(
            model_name='grid',
            name='spring_weight',
        ),
        migrations.AddField(
            model_name='grid',
            name='fuel_assembly_model',
            field=models.ForeignKey(to='tragopan.FuelAssemblyModel', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grid',
            name='inner_sleeve_thickness',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=10, decimal_places=5, help_text='cm', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grid',
            name='outer_sleeve_thickness',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=10, decimal_places=5, help_text='cm', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grid',
            name='side_length',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=10, decimal_places=5, help_text='cm', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grid',
            name='sleeve_height',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=15, decimal_places=5, help_text='g', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grid',
            name='sleeve_material',
            field=models.ForeignKey(to='tragopan.Material', related_query_name='grid_sleeve', related_name='grid_sleeves', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='grid',
            name='spring_material',
            field=models.ForeignKey(to='tragopan.Material', related_query_name='grid_spring', related_name='grid_springs', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='grid',
            name='spring_thickness',
            field=models.DecimalField(help_text='cm', validators=[django.core.validators.MinValueValidator(0)], max_digits=10, decimal_places=5, null=True, blank=True),
        ),
    ]
