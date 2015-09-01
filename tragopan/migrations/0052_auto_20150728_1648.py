# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0051_controlrodassembly_primary'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlRodAssemblyLoadingPattern',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('control_rod_assembly', models.ForeignKey(to='tragopan.ControlRodAssembly')),
                ('cycle', models.ForeignKey(to='tragopan.Cycle', related_name='control_rod_assembly_positions')),
                ('reactor_position', models.ForeignKey(to='tragopan.ReactorPosition')),
            ],
            options={
                'db_table': 'control_rod_assembly_loading_pattern',
            },
        ),
        migrations.AlterUniqueTogether(
            name='controlrodassemblyloadingpattern',
            unique_together=set([('cycle', 'reactor_position')]),
        ),
    ]
