# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0055_auto_20150728_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceAssemblyLoadingPattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('cycle', models.ForeignKey(to='tragopan.Cycle', related_name='source_assembly_positions')),
                ('reactor_position', models.ForeignKey(to='tragopan.ReactorPosition')),
            ],
            options={
                'db_table': 'source_assembly_loading_pattern',
            },
        ),
        migrations.AlterField(
            model_name='sourceassembly',
            name='source_rod_map',
            field=models.ManyToManyField(to='tragopan.FuelAssemblyPosition', through='tragopan.SourceRodMap'),
        ),
        migrations.AlterField(
            model_name='sourcerodmap',
            name='source_assembly',
            field=models.ForeignKey(to='tragopan.SourceAssembly', related_name='source_rod_positions'),
        ),
        migrations.AddField(
            model_name='sourceassemblyloadingpattern',
            name='source_assembly',
            field=models.ForeignKey(to='tragopan.SourceAssembly'),
        ),
        migrations.AlterUniqueTogether(
            name='sourceassemblyloadingpattern',
            unique_together=set([('cycle', 'reactor_position')]),
        ),
    ]
