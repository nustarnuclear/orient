# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0044_auto_20150728_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='BurnablePoisonAssemblyLoadingPattern',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('burnable_poison_assembly', models.ForeignKey(to='tragopan.BurnablePoisonAssembly')),
                ('cycle', models.ForeignKey(to='tragopan.Cycle', related_name='burnable_posison_assembly_positions')),
                ('reactor_position', models.ForeignKey(to='tragopan.ReactorPosition')),
            ],
            options={
                'db_table': 'burnable_poison_assembly_loading_pattern',
            },
        ),
        migrations.RemoveField(
            model_name='claddingtube',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='fakefuelelementtype',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='fuelelement',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='grid',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='guidtube',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='instrumenttube',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='lowercap',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='lowernozzle',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='plenumspring',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='uppercap',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='uppernozzle',
            name='vendor',
        ),
        migrations.AlterField(
            model_name='burnablepoisonrodmap',
            name='burnable_poison_assembly',
            field=models.ForeignKey(to='tragopan.BurnablePoisonAssembly', related_name='rod_positions'),
        ),
        migrations.AlterUniqueTogether(
            name='burnablepoisonassemblyloadingpattern',
            unique_together=set([('reactor_position', 'burnable_poison_assembly')]),
        ),
    ]
