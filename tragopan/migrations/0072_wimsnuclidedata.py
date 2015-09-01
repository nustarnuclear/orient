# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0071_materialcomposition_id_nuclear_lib'),
    ]

    operations = [
        migrations.CreateModel(
            name='WimsNuclideData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('nuclide_name', models.CharField(max_length=30)),
                ('id_wims', models.PositiveSmallIntegerField(unique=True)),
                ('amu', models.DecimalField(decimal_places=6, max_digits=9, validators=[django.core.validators.MinValueValidator(0)])),
                ('nf', models.PositiveSmallIntegerField(choices=[(0, '无共振积分表'), (1, '有共振积分表的非裂变核'), (2, '有共振吸收共振积分表的可裂变核'), (3, '有共振吸收和共振裂变共振积分表的可裂变核'), (4, '没有共振积分表的可裂变核')])),
                ('material_type', models.CharField(max_length=4, choices=[('M', '慢化剂'), ('FP', '裂变产物'), ('A', '锕系核素'), ('B', '可燃核素'), ('D', '用于剂量的材料'), ('S', '结构材料和其他'), ('B/FP', '可燃核素 /裂变产物')])),
                ('descrip', models.CharField(max_length=50)),
                ('element', models.ForeignKey(null=True, blank=True, to='tragopan.Element')),
            ],
            options={
                'db_table': 'wims_nuclide_data',
            },
        ),
    ]
