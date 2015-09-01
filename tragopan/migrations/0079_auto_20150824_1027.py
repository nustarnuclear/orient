# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0078_auto_20150818_1155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='burnablepoisonassembly',
            options={'verbose_name': 'Burnable absorber rod pattern'},
        ),
        migrations.AlterModelOptions(
            name='burnablepoisonassemblyloadingpattern',
            options={'verbose_name': 'Burnable absorber assembly', 'verbose_name_plural': 'Burnable absorber assemblies'},
        ),
        migrations.AlterModelOptions(
            name='burnablepoisonrod',
            options={'verbose_name': 'Burnable absorber rod'},
        ),
        migrations.AlterModelOptions(
            name='controlrodassembly',
            options={'verbose_name_plural': 'Control rod assemblies'},
        ),
        migrations.AlterModelOptions(
            name='controlrodtype',
            options={'verbose_name': 'Control rod'},
        ),
        migrations.AlterModelOptions(
            name='cycle',
            options={'verbose_name': 'Operation cycle'},
        ),
        migrations.AlterModelOptions(
            name='fuelassemblyloadingpattern',
            options={'verbose_name': 'Incore fuel loading pattern'},
        ),
        migrations.AlterModelOptions(
            name='fuelassemblyposition',
            options={'verbose_name': 'Intra-assembly rod pattern'},
        ),
        migrations.AlterModelOptions(
            name='fuelassemblyrepository',
            options={'verbose_name_plural': 'Fuel assembly repository'},
        ),
        migrations.AlterModelOptions(
            name='fuelelementtypeposition',
            options={'verbose_name': 'Intra-assembly fuel element loading pattern'},
        ),
        migrations.AlterModelOptions(
            name='grid',
            options={'verbose_name': 'Fuel grid'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Material repository', 'verbose_name_plural': 'Material repository'},
        ),
        migrations.AlterModelOptions(
            name='nozzleplugassembly',
            options={'verbose_name_plural': 'Nozzle plug assemblies'},
        ),
        migrations.AlterModelOptions(
            name='sourceassembly',
            options={'verbose_name_plural': 'Source assemblies'},
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='plant',
            field=models.ForeignKey(to='tragopan.Plant', related_name='units'),
        ),
    ]
