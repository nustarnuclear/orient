# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tragopan', '0040_auto_20150724_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitparameter',
            name='HFP_core_ave_cool_temp',
            field=models.DecimalField(decimal_places=5, max_digits=15, null=True, blank=True, help_text='unit:K', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='ave_mass_power_density',
            field=models.DecimalField(decimal_places=5, max_digits=15, null=True, blank=True, help_text='unit:KW/Kg (fuel)', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='ave_vol_power_density',
            field=models.DecimalField(decimal_places=5, max_digits=15, null=True, blank=True, help_text='unit:KW/L', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='best_estimated_cool_vol_flow_rate',
            field=models.DecimalField(decimal_places=5, max_digits=15, null=True, blank=True, help_text='unit:m3/h', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='bypass_flow_fraction',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True, blank=True, help_text='unit:%', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
