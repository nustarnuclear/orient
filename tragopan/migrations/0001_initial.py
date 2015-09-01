# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BurnablePoisonAssembly',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'burnable_poison_assembly',
            },
        ),
        migrations.CreateModel(
            name='BurnablePoisonAssemblyNozzlePlug',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('burnable_poison_assembly', models.ForeignKey(to='tragopan.BurnablePoisonAssembly')),
            ],
            options={
                'db_table': 'burnable_poison_assembly_nozzle_plug',
            },
        ),
        migrations.CreateModel(
            name='BurnablePoisonMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('radius', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'burnable_poison_rod_material',
            },
        ),
        migrations.CreateModel(
            name='BurnablePoisonRod',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'burnable_poison_rod',
            },
        ),
        migrations.CreateModel(
            name='BurnablePoisonRodMap',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('burnable_poison_assembly', models.ForeignKey(to='tragopan.BurnablePoisonAssembly')),
                ('burnable_poison_rod', models.ForeignKey(to='tragopan.BurnablePoisonRod')),
            ],
            options={
                'db_table': 'burnable_poison_rod_map',
            },
        ),
        migrations.CreateModel(
            name='CladdingTube',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('roughness', models.DecimalField(max_digits=7, decimal_places=6, blank=True, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', null=True)),
            ],
            options={
                'db_table': 'cladding_tube',
            },
        ),
        migrations.CreateModel(
            name='ControlRodAssembly',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('overall_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'control_rod_assembly',
            },
        ),
        migrations.CreateModel(
            name='ControlRodMap',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('control_rod_assembly', models.ForeignKey(to='tragopan.ControlRodAssembly')),
            ],
            options={
                'db_table': 'control_rod_map',
            },
        ),
        migrations.CreateModel(
            name='ControlRodType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('absorb_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('absorb_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('cladding_inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('cladding_outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'control_rod_type',
            },
        ),
        migrations.CreateModel(
            name='CoreBaffle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('gap_to_fuel', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('thickness', models.DecimalField(max_digits=7, decimal_places=3, blank=True, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', null=True)),
                ('weight', models.DecimalField(max_digits=7, decimal_places=3, blank=True, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:Kg', null=True)),
            ],
            options={
                'db_table': 'core_baffle',
            },
        ),
        migrations.CreateModel(
            name='CoreBarrel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'core_barrel',
            },
        ),
        migrations.CreateModel(
            name='CoreLowerPlate',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:Kg', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'core_lower_plate',
            },
        ),
        migrations.CreateModel(
            name='CoreUpperPlate',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:Kg', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'core_upper_plate',
            },
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('cycle', models.PositiveSmallIntegerField()),
                ('starting_date', models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('shutdown_date', models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('cycle_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:EFPD', max_digits=7, decimal_places=3)),
                ('num_unplanned_shutdowns', models.PositiveSmallIntegerField()),
                ('num_periodical_tests', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'cycle',
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('atomic_number', models.AutoField(serialize=False, primary_key=True)),
                ('symbol', models.CharField(max_length=8, unique=True)),
                ('nameCH', models.CharField(max_length=8)),
                ('nameEN', models.CharField(max_length=40)),
                ('reference', models.CharField(max_length=80, default='IUPAC')),
            ],
            options={
                'db_table': 'element',
                'ordering': ['atomic_number'],
            },
        ),
        migrations.CreateModel(
            name='FakeFuelElementType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('overall_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('pellet_outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('pellet_height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'fake_fuel_element_type',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyLoadingPattern',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('rotation_degree', models.CharField(max_length=3, default='0', choices=[('0', '0'), ('90', '90'), ('180', '180'), ('270', '270')])),
                ('cycle', models.ForeignKey(related_name='fuel_assembly_positions', to='tragopan.Cycle')),
            ],
            options={
                'db_table': 'fuel_assembly_loading_pattern',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model', models.CharField(max_length=5, choices=[('AFA2G', 'AFA2G'), ('AFA3G', 'AFA3G')])),
                ('overall_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('side_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('pin_pitch', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('lower_gap', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('upper_gap', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('licensed_max_discharge_BU', models.DecimalField(max_digits=15, decimal_places=5, blank=True, validators=[django.core.validators.MinValueValidator(0)], help_text='MWd/tU', null=True)),
                ('licensed_pin_discharge_BU', models.DecimalField(max_digits=15, decimal_places=5, blank=True, validators=[django.core.validators.MinValueValidator(0)], help_text='MWd/tU', null=True)),
            ],
            options={
                'db_table': 'fuel_assembly_model',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('row', models.PositiveSmallIntegerField()),
                ('column', models.PositiveSmallIntegerField()),
                ('fuel_assembly_model', models.ForeignKey(related_name='positions', related_query_name='position', to='tragopan.FuelAssemblyModel')),
            ],
            options={
                'db_table': 'fuel_assembly_position',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('PN', models.CharField(max_length=50, unique=True)),
                ('batch_number', models.PositiveSmallIntegerField()),
                ('manufacturing_date', models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('arrival_date', models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('model', models.ForeignKey(to='tragopan.FuelAssemblyModel')),
            ],
            options={
                'db_table': 'fuel_assembly_repository',
            },
        ),
        migrations.CreateModel(
            name='FuelElementMap',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('fuel_assembly_position', models.OneToOneField(to='tragopan.FuelAssemblyPosition')),
            ],
            options={
                'db_table': 'fuel_element_map',
            },
        ),
        migrations.CreateModel(
            name='FuelElementPelletLoadingScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'fuel_element_pellet_loading_scheme',
            },
        ),
        migrations.CreateModel(
            name='FuelElementType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('overall_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('active_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('plenum_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('filling_gas_pressure', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:MPa', max_digits=10, decimal_places=5)),
            ],
            options={
                'db_table': 'fuel_element_type',
            },
        ),
        migrations.CreateModel(
            name='FuelPelletType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('inner_diameter', models.DecimalField(max_digits=7, decimal_places=3, blank=True, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm can be none when hollow', null=True)),
                ('height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('dish_volume_percentage', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', max_digits=9, decimal_places=6)),
                ('dish_height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('dish_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('roughness', models.DecimalField(max_digits=7, decimal_places=6, blank=True, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', null=True)),
                ('density_percentage', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', max_digits=9, decimal_places=6)),
                ('uncertainty_percentage', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', max_digits=9, decimal_places=6)),
                ('coating_thickness', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'fuel_pellet_type',
            },
        ),
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model', models.CharField(max_length=40)),
                ('sleeve_weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='g', max_digits=15, decimal_places=5)),
                ('sleeve_thickness', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='cm', max_digits=10, decimal_places=5)),
                ('spring_weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='g', max_digits=15, decimal_places=5)),
                ('spring_thickness', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='cm', max_digits=10, decimal_places=5)),
                ('functionality', models.CharField(max_length=5, default='fix', choices=[('blend', 'blend'), ('fix', 'fix')])),
            ],
            options={
                'db_table': 'grid',
            },
        ),
        migrations.CreateModel(
            name='GridPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('fuel_assembly_model', models.ForeignKey(to='tragopan.FuelAssemblyModel')),
                ('grid', models.ForeignKey(to='tragopan.Grid')),
            ],
            options={
                'db_table': 'grid_position',
            },
        ),
        migrations.CreateModel(
            name='GuidTube',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('upper_outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('upper_inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('buffer_outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, null=True, decimal_places=3)),
                ('buffer_inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, null=True, decimal_places=3)),
            ],
            options={
                'db_table': 'guid_tube',
            },
        ),
        migrations.CreateModel(
            name='GuidTubeMap',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('fuel_assembly_position', models.OneToOneField(to='tragopan.FuelAssemblyPosition')),
                ('guid_tube', models.ForeignKey(to='tragopan.GuidTube')),
            ],
            options={
                'db_table': 'guid_tube_map',
            },
        ),
        migrations.CreateModel(
            name='InstrumentTube',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'instrument_tube',
            },
        ),
        migrations.CreateModel(
            name='InstrumentTubePosition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('fuel_assembly_position', models.OneToOneField(to='tragopan.FuelAssemblyPosition')),
                ('guid_tube', models.ForeignKey(to='tragopan.InstrumentTube')),
            ],
            options={
                'db_table': 'instrument_tube_position',
            },
        ),
        migrations.CreateModel(
            name='LowerCap',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('fuel_element_type', models.OneToOneField(to='tragopan.FuelElementType')),
            ],
            options={
                'db_table': 'lower_cap',
            },
        ),
        migrations.CreateModel(
            name='LowerNozzle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('pitch', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('plate_thickness', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('plate_porosity', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', max_digits=9, decimal_places=6)),
                ('height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('fuel_assembly_model', models.OneToOneField(to='tragopan.FuelAssemblyModel')),
            ],
            options={
                'db_table': 'lower_nozzle',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('nameCH', models.CharField(max_length=40)),
                ('nameEN', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Material',
            },
        ),
        migrations.CreateModel(
            name='MaterialAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('density', models.DecimalField(max_digits=15, help_text='unit:g/cm3', decimal_places=5)),
                ('heat_capacity', models.DecimalField(max_digits=15, help_text='J/kg*K', decimal_places=5, null=True, blank=True)),
                ('thermal_conductivity', models.DecimalField(max_digits=15, help_text='W/m*K', decimal_places=5, null=True, blank=True)),
                ('expansion_coefficient', models.DecimalField(max_digits=15, help_text='m/K', decimal_places=5, null=True, blank=True)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('material', models.OneToOneField(to='tragopan.Material', related_name='attribute')),
            ],
            options={
                'db_table': 'material_attribute',
            },
        ),
        migrations.CreateModel(
            name='MaterialComposition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight_percent', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', max_digits=9, decimal_places=6)),
                ('element', models.ForeignKey(to_field='symbol', to='tragopan.Element')),
                ('material', models.ForeignKey(related_name='elements', related_query_name='element', to='tragopan.Material')),
            ],
            options={
                'db_table': 'material_composition',
                'ordering': ['material'],
            },
        ),
        migrations.CreateModel(
            name='MaterialNuclide',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight_percent', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', max_digits=9, decimal_places=6)),
                ('material', models.ForeignKey(related_name='nuclides', related_query_name='nuclide', to='tragopan.Material')),
            ],
            options={
                'db_table': 'material_nuclide',
            },
        ),
        migrations.CreateModel(
            name='NozzlePlugAssembly',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:Kg', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'nozzle_plug_assembly',
            },
        ),
        migrations.CreateModel(
            name='NozzlePlugRod',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('material', models.ForeignKey(to='tragopan.Material')),
            ],
            options={
                'db_table': 'nozzle_plug_rod',
            },
        ),
        migrations.CreateModel(
            name='NozzlePlugRodMap',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('guid_tube_position', models.OneToOneField(to='tragopan.GuidTubeMap')),
                ('nozzle_plug_assembly', models.ForeignKey(to='tragopan.NozzlePlugAssembly')),
                ('nozzle_plug_rod', models.ForeignKey(to='tragopan.NozzlePlugRod')),
            ],
            options={
                'db_table': 'nozzle_plug_rod_map',
            },
        ),
        migrations.CreateModel(
            name='Nuclide',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('atom_mass', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=9, decimal_places=6)),
                ('abundance', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', max_digits=9, decimal_places=6)),
                ('reference', models.CharField(max_length=80, default='IUPAC')),
                ('element', models.ForeignKey(related_name='nuclides', to_field='symbol', related_query_name='nuclide', to='tragopan.Element')),
            ],
            options={
                'db_table': 'Nuclide',
                'ordering': ['element'],
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('nameCH', models.CharField(max_length=40)),
                ('abbrCH', models.CharField(max_length=40)),
                ('nameEN', models.CharField(max_length=40)),
                ('abbrEN', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'plant',
            },
        ),
        migrations.CreateModel(
            name='PlenumSpring',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:g', max_digits=10, decimal_places=3)),
                ('outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=5)),
                ('wire_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=5)),
                ('fuel_element_type', models.OneToOneField(to='tragopan.FuelElementType')),
                ('material', models.ForeignKey(to='tragopan.Material')),
            ],
            options={
                'db_table': 'plenum_spring',
            },
        ),
        migrations.CreateModel(
            name='PressureVessel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('weld_thickness', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('base_material', models.ForeignKey(related_name='pressure_vessel_base', to='tragopan.Material')),
            ],
            options={
                'db_table': 'pressure_vessel',
            },
        ),
        migrations.CreateModel(
            name='PressureVesselInsulation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('material', models.ForeignKey(to='tragopan.Material')),
            ],
            options={
                'db_table': 'pressure_vessel_insulation',
            },
        ),
        migrations.CreateModel(
            name='ReactorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model', models.CharField(max_length=50, choices=[('QNPC2', 'QNPC2'), ('QNPC1', 'QNPC1'), ('M310', 'M310'), ('CAP1000', 'CAP1000'), ('AP1000', 'AP1000')])),
                ('generation', models.CharField(max_length=2, choices=[('2', '2'), ('2+', '2+'), ('3', '3')])),
                ('reactor_type', models.CharField(max_length=3, choices=[('PWR', 'PWR'), ('BWR', 'BWR')])),
                ('geometry_type', models.CharField(max_length=9, choices=[('Cartesian', 'Cartesian'), ('Hexagonal', 'Hexagonal')])),
                ('row_symbol', models.CharField(max_length=6, choices=[('Number', 'Number'), ('Letter', 'Letter')])),
                ('column_symbol', models.CharField(max_length=6, choices=[('Number', 'Number'), ('Letter', 'Letter')])),
                ('num_loops', models.PositiveSmallIntegerField()),
                ('num_control_rod_mechanisms', models.PositiveSmallIntegerField()),
                ('core_equivalent_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('active_height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('cold_state_assembly_pitch', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=4)),
                ('hot_state_assembly_pitch', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=4)),
            ],
            options={
                'db_table': 'reactor_model',
            },
        ),
        migrations.CreateModel(
            name='ReactorPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('row', models.PositiveSmallIntegerField()),
                ('column', models.PositiveSmallIntegerField()),
                ('reactor_model', models.ForeignKey(related_name='positions', related_query_name='position', to='tragopan.ReactorModel')),
            ],
            options={
                'db_table': 'reactor_position',
            },
        ),
        migrations.CreateModel(
            name='RipPlate',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('thickness', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('width', models.DecimalField(max_digits=7, decimal_places=3, blank=True, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', null=True)),
                ('core_baffle', models.OneToOneField(to='tragopan.ReactorModel')),
                ('material', models.ForeignKey(to='tragopan.Material')),
            ],
            options={
                'db_table': 'rip_plate',
            },
        ),
        migrations.CreateModel(
            name='SourceAssembly',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'source_assembly',
            },
        ),
        migrations.CreateModel(
            name='SourceAssemblyBPRod',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('burnable_poison_rod', models.ForeignKey(to='tragopan.BurnablePoisonRod')),
                ('guid_tube_position', models.OneToOneField(to='tragopan.GuidTubeMap')),
                ('source_assembly', models.ForeignKey(to='tragopan.SourceAssembly')),
            ],
            options={
                'db_table': 'source_bp_rod',
            },
        ),
        migrations.CreateModel(
            name='SourceAssemblyNozzlePlug',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('guid_tube_position', models.OneToOneField(to='tragopan.GuidTubeMap')),
                ('nozzle_plug_rod', models.ForeignKey(to='tragopan.NozzlePlugRod')),
                ('source_assembly', models.ForeignKey(to='tragopan.SourceAssembly')),
            ],
            options={
                'db_table': 'source_assembly_nozzle_plug',
            },
        ),
        migrations.CreateModel(
            name='SourceRodMap',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('guid_tube_position', models.OneToOneField(to='tragopan.GuidTubeMap')),
                ('source_assembly', models.ForeignKey(to='tragopan.SourceAssembly')),
            ],
            options={
                'db_table': 'source_rod_map',
            },
        ),
        migrations.CreateModel(
            name='SourceRodType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('type', models.CharField(max_length=9, choices=[('primary', 'primary'), ('secondary', 'secondary')])),
                ('overall_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('strength', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=7, decimal_places=3)),
                ('material', models.ForeignKey(to='tragopan.Material')),
            ],
            options={
                'db_table': 'source_rod_type',
            },
        ),
        migrations.CreateModel(
            name='ThermalShield',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('angle', models.DecimalField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(360)], help_text='unit:degree', max_digits=7, decimal_places=3)),
                ('loc_height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('loc_theta', models.DecimalField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(360)], help_text='unit:degree', max_digits=7, decimal_places=3)),
                ('gap_to_barrel', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('material', models.ForeignKey(to='tragopan.Material')),
                ('reactor_model', models.ForeignKey(to='tragopan.ReactorModel')),
            ],
            options={
                'db_table': 'thermal_shield',
            },
        ),
        migrations.CreateModel(
            name='UnitParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('unit', models.PositiveSmallIntegerField()),
                ('electric_power', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:MW', max_digits=10, decimal_places=3)),
                ('thermal_power', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:MW', max_digits=10, decimal_places=3)),
                ('heat_fraction_in_fuel', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', max_digits=9, decimal_places=6)),
                ('primary_system_pressure', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:MPa', max_digits=15, decimal_places=5)),
                ('ave_linear_power_density', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:KW/m', max_digits=15, decimal_places=5)),
                ('ave_vol_power_density', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:KW/L', max_digits=15, decimal_places=5)),
                ('ave_mass_power_density', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:KW/Kg (fuel)', max_digits=15, decimal_places=5)),
                ('best_estimated_cool_vol_flow_rate', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:m3/h', max_digits=15, decimal_places=5)),
                ('bypass_flow_fraction', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', max_digits=9, decimal_places=6)),
                ('cold_state_cool_temp', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:K', max_digits=15, decimal_places=5)),
                ('HZP_cool_inlet_temp', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:K', max_digits=15, decimal_places=5)),
                ('HFP_cool_inlet_temp', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:K', max_digits=15, decimal_places=5)),
                ('HFP_core_ave_cool_temp', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:K', max_digits=15, decimal_places=5)),
                ('mid_power_cool_inlet_temp', models.DecimalField(max_digits=15, decimal_places=5, blank=True, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:K', null=True)),
                ('plant', models.ForeignKey(to='tragopan.Plant')),
                ('reactor_model', models.ForeignKey(to='tragopan.ReactorModel')),
            ],
            options={
                'db_table': 'unit_parameter',
            },
        ),
        migrations.CreateModel(
            name='UpperCap',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('fuel_element_type', models.OneToOneField(to='tragopan.FuelElementType')),
                ('material', models.ForeignKey(to='tragopan.Material')),
            ],
            options={
                'db_table': 'upper_cap',
            },
        ),
        migrations.CreateModel(
            name='UpperNozzle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('pitch', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('plate_thickness', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('plate_porosity', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', max_digits=9, decimal_places=6)),
                ('height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('fuel_assembly_model', models.OneToOneField(to='tragopan.FuelAssemblyModel')),
                ('material', models.ForeignKey(to='tragopan.Material')),
            ],
            options={
                'db_table': 'upper_nozzle',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('nameCH', models.CharField(max_length=40)),
                ('abbrCH', models.CharField(max_length=40)),
                ('nameEN', models.CharField(max_length=40)),
                ('abbrEN', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=12, default='Designer', choices=[('Designer', 'Designer'), ('Manufacturer', 'Manufacturer'), ('Material', 'Material')])),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
        migrations.AddField(
            model_name='uppernozzle',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='uppercap',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='thermalshield',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='sourcerodmap',
            name='source_rod',
            field=models.ForeignKey(to='tragopan.SourceRodType'),
        ),
        migrations.AddField(
            model_name='sourceassembly',
            name='burnable_poison_map',
            field=models.ManyToManyField(related_name='source_burnable_poison', to='tragopan.GuidTubeMap', through='tragopan.SourceAssemblyBPRod'),
        ),
        migrations.AddField(
            model_name='sourceassembly',
            name='nozzle_plug_rod_map',
            field=models.ManyToManyField(related_name='source_nozzle_plug', to='tragopan.GuidTubeMap', through='tragopan.SourceAssemblyNozzlePlug'),
        ),
        migrations.AddField(
            model_name='sourceassembly',
            name='source_rod_map',
            field=models.ManyToManyField(related_name='source_rod', to='tragopan.GuidTubeMap', through='tragopan.SourceRodMap'),
        ),
        migrations.AddField(
            model_name='reactormodel',
            name='incore_instrument_position',
            field=models.ManyToManyField(db_table='incore_instrument_map', related_name='incore_instrument_position', to='tragopan.ReactorPosition', blank=True),
        ),
        migrations.AddField(
            model_name='reactormodel',
            name='thermal_couple_position',
            field=models.ManyToManyField(db_table='thermal_couple_map', related_name='thermal_couple_position', to='tragopan.ReactorPosition', blank=True),
        ),
        migrations.AddField(
            model_name='reactormodel',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='pressurevesselinsulation',
            name='reactor_model',
            field=models.OneToOneField(to='tragopan.ReactorModel'),
        ),
        migrations.AddField(
            model_name='pressurevesselinsulation',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='pressurevessel',
            name='reactor_model',
            field=models.OneToOneField(to='tragopan.ReactorModel'),
        ),
        migrations.AddField(
            model_name='pressurevessel',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='pressurevessel',
            name='weld_material',
            field=models.ForeignKey(related_name='pressure_vessel_weld', to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='plenumspring',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='nozzleplugassembly',
            name='nozzle_plug_rod',
            field=models.ManyToManyField(to='tragopan.NozzlePlugRod', through='tragopan.NozzlePlugRodMap'),
        ),
        migrations.AddField(
            model_name='materialnuclide',
            name='nuclide',
            field=models.ForeignKey(to='tragopan.Nuclide'),
        ),
        migrations.AddField(
            model_name='material',
            name='material_composition',
            field=models.ManyToManyField(to='tragopan.Element', through='tragopan.MaterialComposition'),
        ),
        migrations.AddField(
            model_name='lowernozzle',
            name='material',
            field=models.ForeignKey(to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='lowernozzle',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='lowercap',
            name='material',
            field=models.ForeignKey(to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='lowercap',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='instrumenttube',
            name='material',
            field=models.ForeignKey(to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='instrumenttube',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='guidtube',
            name='material',
            field=models.ForeignKey(to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='guidtube',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='grid',
            name='sleeve_material',
            field=models.ForeignKey(related_name='grid_sleeves', related_query_name='grid_sleeve', to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='grid',
            name='spring_material',
            field=models.ForeignKey(related_name='grid_springs', related_query_name='grid_spring', to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='grid',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='fuelpellettype',
            name='coating_material',
            field=models.ForeignKey(related_name='fuel_pellet_coating', to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='fuelpellettype',
            name='material',
            field=models.ForeignKey(related_name='fuel_pellet_material', to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='fuelelementtype',
            name='filling_gas_materia',
            field=models.ForeignKey(to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='fuelelementtype',
            name='fuel_pellet',
            field=models.ManyToManyField(to='tragopan.FuelPelletType', through='tragopan.FuelElementPelletLoadingScheme'),
        ),
        migrations.AddField(
            model_name='fuelelementtype',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='fuelelementpelletloadingscheme',
            name='fuel_element_type',
            field=models.ForeignKey(to='tragopan.FuelElementType'),
        ),
        migrations.AddField(
            model_name='fuelelementpelletloadingscheme',
            name='fuel_pellet_type',
            field=models.ForeignKey(to='tragopan.FuelPelletType'),
        ),
        migrations.AddField(
            model_name='fuelelementmap',
            name='fuel_element_type',
            field=models.ForeignKey(to='tragopan.FuelElementType'),
        ),
        migrations.AddField(
            model_name='fuelassemblyrepository',
            name='plant',
            field=models.ForeignKey(to='tragopan.Plant'),
        ),
        migrations.AddField(
            model_name='fuelassemblyrepository',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='fuelassemblymodel',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='fuelassemblyloadingpattern',
            name='fuel_assembly',
            field=models.ForeignKey(to='tragopan.FuelAssemblyRepository'),
        ),
        migrations.AddField(
            model_name='fuelassemblyloadingpattern',
            name='reactor_position',
            field=models.ForeignKey(to='tragopan.ReactorPosition'),
        ),
        migrations.AddField(
            model_name='fakefuelelementtype',
            name='material',
            field=models.ForeignKey(to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='fakefuelelementtype',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='cycle',
            name='unit',
            field=models.ForeignKey(to='tragopan.UnitParameter'),
        ),
        migrations.AddField(
            model_name='coreupperplate',
            name='material',
            field=models.ForeignKey(to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='coreupperplate',
            name='reactor_model',
            field=models.OneToOneField(to='tragopan.ReactorModel'),
        ),
        migrations.AddField(
            model_name='coreupperplate',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='corelowerplate',
            name='material',
            field=models.ForeignKey(to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='corelowerplate',
            name='reactor_model',
            field=models.OneToOneField(to='tragopan.ReactorModel'),
        ),
        migrations.AddField(
            model_name='corelowerplate',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='corebarrel',
            name='material',
            field=models.ForeignKey(to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='corebarrel',
            name='reactor_model',
            field=models.OneToOneField(to='tragopan.ReactorModel'),
        ),
        migrations.AddField(
            model_name='corebarrel',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='corebaffle',
            name='material',
            field=models.ForeignKey(to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='corebaffle',
            name='reactor_model',
            field=models.OneToOneField(to='tragopan.ReactorModel'),
        ),
        migrations.AddField(
            model_name='corebaffle',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='controlrodtype',
            name='absorb_material',
            field=models.ForeignKey(related_name='control_rod_absorb', to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='controlrodtype',
            name='cladding_material',
            field=models.ForeignKey(related_name='control_rod_cladding', to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='controlrodmap',
            name='control_rod_type',
            field=models.ForeignKey(to='tragopan.ControlRodType'),
        ),
        migrations.AddField(
            model_name='controlrodmap',
            name='guid_tube_position',
            field=models.OneToOneField(to='tragopan.GuidTubeMap'),
        ),
        migrations.AddField(
            model_name='controlrodassembly',
            name='control_rod_map',
            field=models.ManyToManyField(to='tragopan.GuidTubeMap', through='tragopan.ControlRodMap'),
        ),
        migrations.AddField(
            model_name='claddingtube',
            name='fuel_element_type',
            field=models.OneToOneField(to='tragopan.FuelElementType'),
        ),
        migrations.AddField(
            model_name='claddingtube',
            name='material',
            field=models.ForeignKey(to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='claddingtube',
            name='vendor',
            field=models.ForeignKey(to='tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='burnablepoisonrodmap',
            name='guid_tube_position',
            field=models.OneToOneField(to='tragopan.GuidTubeMap'),
        ),
        migrations.AddField(
            model_name='burnablepoisonrod',
            name='radial_map',
            field=models.ManyToManyField(related_name='burnable_poison_rod', to='tragopan.Material', through='tragopan.BurnablePoisonMaterial'),
        ),
        migrations.AddField(
            model_name='burnablepoisonmaterial',
            name='burnable_poison_rod',
            field=models.ForeignKey(to='tragopan.BurnablePoisonRod'),
        ),
        migrations.AddField(
            model_name='burnablepoisonmaterial',
            name='material',
            field=models.ForeignKey(to='tragopan.Material'),
        ),
        migrations.AddField(
            model_name='burnablepoisonassemblynozzleplug',
            name='guid_tube_position',
            field=models.OneToOneField(to='tragopan.GuidTubeMap'),
        ),
        migrations.AddField(
            model_name='burnablepoisonassemblynozzleplug',
            name='nozzle_plug_rod',
            field=models.ForeignKey(to='tragopan.NozzlePlugRod'),
        ),
        migrations.AddField(
            model_name='burnablepoisonassembly',
            name='burnable_poison_map',
            field=models.ManyToManyField(related_name='bp_burnable_poison', to='tragopan.GuidTubeMap', through='tragopan.BurnablePoisonRodMap'),
        ),
        migrations.AddField(
            model_name='burnablepoisonassembly',
            name='nozzle_plug_rod_map',
            field=models.ManyToManyField(related_name='bp_nozzle_plug', to='tragopan.GuidTubeMap', through='tragopan.BurnablePoisonAssemblyNozzlePlug'),
        ),
        migrations.AlterUniqueTogether(
            name='unitparameter',
            unique_together=set([('plant', 'unit')]),
        ),
        migrations.AlterUniqueTogether(
            name='reactorposition',
            unique_together=set([('reactor_model', 'row', 'column')]),
        ),
        migrations.AlterUniqueTogether(
            name='nuclide',
            unique_together=set([('element', 'atom_mass')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='nuclide',
            order_with_respect_to='element',
        ),
        migrations.AlterUniqueTogether(
            name='materialcomposition',
            unique_together=set([('material', 'element')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='materialcomposition',
            order_with_respect_to='material',
        ),
        migrations.AlterUniqueTogether(
            name='fuelassemblyposition',
            unique_together=set([('fuel_assembly_model', 'row', 'column')]),
        ),
        migrations.AlterUniqueTogether(
            name='fuelassemblyloadingpattern',
            unique_together=set([('cycle', 'reactor_position')]),
        ),
        migrations.AlterUniqueTogether(
            name='cycle',
            unique_together=set([('cycle', 'unit')]),
        ),
    ]
