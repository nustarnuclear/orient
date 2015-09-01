# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0005_auto_20150716_2146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nuclide',
            options={'ordering': ['element']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='nuclide',
            order_with_respect_to=None,
        ),
    ]
