# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import calculation.models


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0066_auto_20150807_1932'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calculation', '0002_auto_20150811_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='RobinFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('file_type', models.CharField(choices=[('BASE_FUEL', 'BASE_FUEL'), ('BP_OUT', 'BP_OUT'), ('BR', 'BR')], max_length=9)),
                ('input_file', models.FileField(upload_to=calculation.models.get_robin_upload_path)),
                ('out1_file', models.FileField(upload_to=calculation.models.get_robin_upload_path)),
                ('log_file', models.FileField(upload_to=calculation.models.get_robin_upload_path)),
                ('burnable_poison_assembly', models.ForeignKey(null=True, blank=True, to='tragopan.BurnablePoisonAssembly')),
                ('fuel_assembly_type', models.ForeignKey(to='tragopan.FuelAssemblyType')),
                ('plant', models.ForeignKey(to='tragopan.Plant')),
                ('user', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'robin_file',
            },
        ),
        migrations.AlterModelOptions(
            name='ibis',
            options={'verbose_name_plural': 'Ibis'},
        ),
        migrations.AlterModelOptions(
            name='prerobinbranch',
            options={'verbose_name_plural': 'branches'},
        ),
        migrations.AlterOrderWithRespectTo(
            name='robinfile',
            order_with_respect_to='fuel_assembly_type',
        ),
    ]
