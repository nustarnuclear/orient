# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0089_remove_materialcomposition_element'),
    ]

    operations = [
        migrations.CreateModel(
            name='MixtureComposition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight_percent', models.DecimalField(decimal_places=6, max_digits=9, help_text='unit:%', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('material', models.ForeignKey(to='tragopan.Material')),
                ('mixture', models.ForeignKey(related_name='mixtures', to='tragopan.Material', related_query_name='mixture')),
            ],
            options={
                'db_table': 'mixture_composition',
            },
        ),
        migrations.AddField(
            model_name='material',
            name='mixture_composition',
            field=models.ManyToManyField(through='tragopan.MixtureComposition', to='tragopan.Material'),
        ),
    ]
