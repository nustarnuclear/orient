# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0024_auto_20150721_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelPelletType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('material', models.ForeignKey(related_name='fuel_pellet_material', to='tragopan.Material')),
            ],
            options={
                'db_table': 'fuel_pellet_type',
            },
        ),
        migrations.RemoveField(
            model_name='fuelpellet',
            name='material',
        ),
        migrations.AddField(
            model_name='fuelpellettype',
            name='model',
            field=models.ForeignKey(to='tragopan.FuelPellet'),
        ),
    ]
