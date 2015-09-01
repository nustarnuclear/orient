# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0060_auto_20150729_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideTube',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('upper_outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, help_text='unit:cm', max_digits=7)),
                ('upper_inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, help_text='unit:cm', max_digits=7)),
                ('buffer_outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=7, help_text='unit:cm', decimal_places=3, null=True)),
                ('buffer_inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=7, help_text='unit:cm', decimal_places=3, null=True)),
                ('fuel_assembly_model', models.OneToOneField(to='tragopan.FuelAssemblyModel')),
                ('material', models.ForeignKey(to='tragopan.Material')),
            ],
            options={
                'db_table': 'guide_tube',
            },
        ),
        migrations.RemoveField(
            model_name='guidtube',
            name='fuel_assembly_model',
        ),
        migrations.RemoveField(
            model_name='guidtube',
            name='material',
        ),
        migrations.DeleteModel(
            name='GuidTube',
        ),
    ]
