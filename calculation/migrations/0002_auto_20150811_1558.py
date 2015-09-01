# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import calculation.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tragopan', '0066_auto_20150807_1932'),
        ('calculation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ibis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('ibis_file', models.FileField(upload_to=calculation.models.get_ibis_upload_path)),
                ('reactor_model', models.ForeignKey(to='tragopan.ReactorModel')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'db_table': 'ibis',
            },
        ),
        migrations.AlterOrderWithRespectTo(
            name='ibis',
            order_with_respect_to='reactor_model',
        ),
    ]
