from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from tragopan.models import ReactorModel
from django.conf import settings
import os
# Create your models here.

def get_ibis_upload_path(instance,filename):
    plant_name=instance.plant.abbrEN
    
    return "{}/ibis_files/{}".format(plant_name,filename)

def get_robin_upload_path(instance,filename):
    plant_name=instance.plant.abbrEN
    file_type=instance.file_type
    assembly_name=instance.fuel_assembly_type.model.name
    enrichment=instance.fuel_assembly_type.assembly_enrichment
    
    if instance.burnable_poison_assembly:
        str_num=str(instance.burnable_poison_assembly.rod_positions.count())
    else:
        str_num='00'
        
    tmp=str(int(enrichment*1000))+str_num
    
    return "{}/robin_files/{}/{}/{}/{}".format(plant_name,file_type,assembly_name,tmp,filename)

def get_pre_robin_upload_path(instance,filename):
    plant_name=instance.plant.abbrEN
    file_type=instance.file_type
    assembly_name=instance.fuel_assembly_type.model.name
    enrichment=instance.fuel_assembly_type.assembly_enrichment
    
    if instance.burnable_poison_assembly:
        str_num=str(instance.burnable_poison_assembly.rod_positions.count())
    else:
        str_num='00'
        
    tmp=str(int(enrichment*1000))+str_num
    
    return "{}/pre_robin_files/{}/{}/{}/{}".format(plant_name,file_type,assembly_name,tmp,filename)


FILE_TYPE_CHOICES=(
                    ('BASE_FUEL','BASE_FUEL'),
                    ('BP_OUT','BP_OUT'),
                    ('BR','BR'),
    )

 
# base model to contain the basic information
class BaseModel(models.Model):
    time_inserted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    remark = models.TextField(blank=True)
    user=models.ForeignKey(User,blank=True,null=True)
    class Meta:
        abstract=True

#concrete model in DATABASE

    
class PreRobinModel(BaseModel):
    
    DEP_STRATEGY_CHOICES=(
                          ('LLR','LLR'),
                          ('PPC','PPC'),
                          ('LR','LR'),
                          ('PC','PC'),
    )
    POLAR_TYPE_CHOICES=(
                        ('LCMD','LCMD'),
                        ('TYPL','TYPL'),
                        ('DeCT','DeCT'),
    )
    LEAKAGE_PATH_CHOICES=(
                          (0,0),
                          (1,1),
                          (2,2),
    )
    LEAKAGE_METHOD_CHOICES=(
                            ('B1','B1'),
                            ('P1','P1'),
    )
    CONDENSATION_PATH_CHOICES=(
                               (0,0),
                               (1,1),
                               (2,2),
    )
    NUM_GROUP_2D_CHIOCES=(
                          (2,2),
                          (3,3),
                          (4,4),
                          (8,8),
                          (18,18),
                          (25,25),
                          (33,33),
    )
   
   
    
    model_name=models.CharField(max_length=32)
    

   
    #depletion state
    system_pressure=models.DecimalField(max_digits=7,decimal_places=5,default=15.51,validators=[MinValueValidator(0)],help_text='MPa')
    dep_strategy=models.CharField(max_length=3,choices=DEP_STRATEGY_CHOICES,default='LLR',blank=True,null=True)
  
    
    #accuracy_control
    track_density=models.DecimalField(max_digits=5,decimal_places=5,default=0.03,validators=[MinValueValidator(0)],help_text='cm')
    polar_type=models.CharField(max_length=4,choices=POLAR_TYPE_CHOICES,default='LCMD')
    polar_azimuth=models.CommaSeparatedIntegerField(max_length=50,default='4,16')
    iter_inner=models.PositiveSmallIntegerField(default=3)
    iter_outer=models.PositiveSmallIntegerField(default=100)
    eps_keff=models.DecimalField(max_digits=5,decimal_places=5,validators=[MinValueValidator(0)],default=1e-5)
    eps_flux=models.DecimalField(max_digits=5,decimal_places=5,validators=[MinValueValidator(0)],default=1e-4)
    #fundamental_mode
    leakage_corrector_path=models.PositiveSmallIntegerField(choices=LEAKAGE_PATH_CHOICES,default=2)
    leakage_corrector_method=models.CharField(max_length=2,choices=LEAKAGE_METHOD_CHOICES,default='B1')
    buckling_or_keff=models.DecimalField(max_digits=10,decimal_places=5,default=1)
    #energy_condensation
    condensation_path=models.PositiveSmallIntegerField(choices=CONDENSATION_PATH_CHOICES,default=1)
    num_group_2D=models.PositiveSmallIntegerField(choices=NUM_GROUP_2D_CHIOCES,default=25)
    #edit_control
    num_group_edit=models.PositiveSmallIntegerField(choices=NUM_GROUP_2D_CHIOCES,default=2)
    micro_xs_output=models.BooleanField(default=False)
    class Meta:
        db_table='pre_robin_model'
    
    def __str__(self):
        return self.model_name
      

class PreRobinInput(BaseModel):
    NUM_FUEL_CHOICES=(
                 (1,1),
                 (2,2),
                 (3,3),
    )
    NUM_EDIT_NODE_CHOICES=(
                        (16,16),
                        (4,4),
    )
    
    segment_identity=models.CharField(max_length=32)
    plant=models.ForeignKey('tragopan.Plant')
    file_type=models.CharField(max_length=9,choices=FILE_TYPE_CHOICES)
    use_pre_segment=models.ForeignKey('self',blank=True,null=True)
    pre_robin_model=models.ForeignKey(PreRobinModel,default=1)
    fuel_assembly_type=models.ForeignKey('tragopan.FuelAssemblyType')
    burnable_poison_assembly=models.ForeignKey('tragopan.BurnablePoisonAssembly',blank=True,null=True)
    grid=models.ForeignKey('tragopan.Grid',blank=True,null=True)
    
    #depletion computation
    power_density=models.DecimalField(max_digits=10,decimal_places=5,validators=[MinValueValidator(0)],help_text='w/g',blank=True,null=True)
    assembly_maxium_burnup=models.DecimalField(max_digits=7,decimal_places=5,validators=[MinValueValidator(0),MaxValueValidator(100)],help_text='GWd/tU',blank=True,null=True)
    boron_density=models.DecimalField(max_digits=10,decimal_places=5,validators=[MinValueValidator(0)],help_text='ppm',blank=True,null=True)
    moderator_temperature=models.DecimalField(max_digits=10,decimal_places=5,validators=[MinValueValidator(0)],help_text='K',blank=True,null=True)
    fuel_temperature=models.DecimalField(max_digits=10,decimal_places=5,validators=[MinValueValidator(0)],help_text='K',blank=True,null=True)
    
    #reflector model computation
    core_baffle=models.ForeignKey('tragopan.CoreBaffle',blank=True,null=True)
    num_fuel_assembly=models.PositiveSmallIntegerField(choices=NUM_FUEL_CHOICES,blank=True,null=True)
    num_edit_node=models.PositiveSmallIntegerField(default=16,choices=NUM_EDIT_NODE_CHOICES,blank=True,null=True)
    #branch computation
    branch_composition=models.ManyToManyField('PreRobinBranch',related_name='branches')
    #prerobin file
    pre_robin_file=models.FileField(upload_to=get_pre_robin_upload_path,blank=True,null=True)
   
    class Meta:
        db_table='pre_robin_input'
    
    def __str__(self):
        return self.segment_identity
        

class PreRobinBranch(models.Model):
    identity=models.CharField(max_length=32)
    #the default burnup point for BOR TMO TFU CRD
    #boron density branch
    max_boron_density=models.PositiveSmallIntegerField(help_text='ppm',blank=True,null=True)
    min_boron_density=models.PositiveSmallIntegerField(default=0,help_text='ppm',blank=True,null=True)
    boron_density_interval=models.PositiveSmallIntegerField(help_text='ppm',default=200,blank=True,null=True)
    #fuel temperature branch
    max_fuel_temperature=models.PositiveSmallIntegerField(help_text='K',blank=True,null=True)
    min_fuel_temperature=models.PositiveSmallIntegerField(help_text='K',blank=True,null=True)
    fuel_temperature_interval=models.PositiveSmallIntegerField(help_text='K',default=50,blank=True,null=True)
    #moderator temperature branch
    max_moderator_temperature=models.PositiveSmallIntegerField(help_text='K',blank=True,null=True)
    min_moderator_temperature=models.PositiveSmallIntegerField(help_text='K',blank=True,null=True)
    moderator_temperature_interval=models.PositiveSmallIntegerField(help_text='K',default=4,blank=True,null=True)
    #control rod assembly branch(the even integer of default burnup) 
    control_rod_assembly=models.ForeignKey('tragopan.ControlRodAssembly',blank=True,null=True)
    #shutdown cooling branch(the even integer of default burnup) 
    shutdown_cooling_days=models.PositiveSmallIntegerField(blank=True,null=True,help_text='day')
    #xenon branch(the even integer of default burnup) 
    xenon=models.BooleanField(default=False,verbose_name='set xenon density to 0?',)
    class Meta:
        db_table='pre_robin_branch'
        verbose_name_plural='branches'
        
    def __str__(self):
        return self.identity

  
class Ibis(BaseModel):
    plant=models.ForeignKey('tragopan.Plant')
    ibis_name=models.CharField(max_length=32)
    fuel_assembly_type=models.ForeignKey('tragopan.FuelAssemblyType')
    reactor_model=models.ForeignKey('tragopan.ReactorModel')
    burnable_poison_assembly=models.ForeignKey('tragopan.BurnablePoisonAssembly',blank=True,null=True)
    active_length=models.DecimalField(max_digits=10, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm',default=365.80000)
    ibis_file=models.FileField(upload_to=get_ibis_upload_path)
    
    
    
    
    class Meta:
        db_table='ibis'
        order_with_respect_to='reactor_model'
        verbose_name_plural='Ibis'
        
    def __str__(self):
        return '{}'.format(self.ibis_name)
    

class RobinFile(BaseModel):
   
    plant=models.ForeignKey('tragopan.Plant')
    file_type=models.CharField(max_length=9,choices=FILE_TYPE_CHOICES)
    fuel_assembly_type=models.ForeignKey('tragopan.FuelAssemblyType')
    burnable_poison_assembly=models.ForeignKey('tragopan.BurnablePoisonAssembly',blank=True,null=True)
    input_file=models.FileField(upload_to=get_robin_upload_path)
    out1_file=models.FileField(upload_to=get_robin_upload_path)
    log_file=models.FileField(upload_to=get_robin_upload_path)
    
    class Meta:
        db_table='robin_file'
        order_with_respect_to='fuel_assembly_type'
        
        
    def __str__(self):
        return '{}'.format(self.fuel_assembly_type)

    
class BaseFuel(BaseModel):
    fuel_identity=models.CharField(max_length=32)
    offset=models.BooleanField(default=False)
    base_bottom=models.DecimalField(max_digits=10,decimal_places=5,validators=[MinValueValidator(0)],help_text='cm',default=0)
    axial_composition=models.ManyToManyField(Ibis,through='BaseFuelComposition')
    
    def if_insert_burnable_fuel(self):
        obj=BaseFuel.objects.get(pk=self.pk)
        composition=obj.composition.count()
        result=True if composition>1 else False
        return result
    
    class Meta:
        db_table='base_fuel'
        
        
        
    def __str__(self):
        return '{}'.format(self.fuel_identity)
    
class BaseFuelComposition(models.Model):
    base_fuel=models.ForeignKey(BaseFuel,related_name='composition')
    ibis=models.ForeignKey(Ibis,related_name='base_fuels')
    height=models.DecimalField(max_digits=10,decimal_places=5,validators=[MinValueValidator(0)],help_text='cm',)
    class Meta:
        db_table='base_fuel_composition'
        
        
        
    def __str__(self):
        return '{}'.format(self.base_fuel)
    

#egret task    
def get_egret_base_core_xml_path(instance,filename):
    unit=instance.unit
    reactor_model=unit.reactor_model
    reactor_model_name=reactor_model.name
    plant_name=unit.plant.abbrEN
    return '{}/{}'.format(reactor_model_name,filename)

def get_egret_base_component_xml_path(instance,filename):
    unit=instance.unit
    reactor_model=unit.reactor_model
    reactor_model_name=reactor_model.name
    plant_name=unit.plant.abbrEN
    return '{}/unit{}/{}'.format(reactor_model_name,unit.unit, filename)       

def get_egret_loading_pattern_xml_path(instance,filename):
    unit=instance.unit
    reactor_model=unit.reactor_model
    reactor_model_name=reactor_model.name
    plant_name=unit.plant.abbrEN
    return '{}/unit{}/{}'.format(reactor_model_name,unit.unit, filename)   

class EgretInputXML(models.Model):
    unit=models.ForeignKey('tragopan.UnitParameter')
    base_component_xml=models.FileField(upload_to=get_egret_base_component_xml_path)
    base_core_xml=models.FileField(upload_to=get_egret_base_core_xml_path)
    loading_pattern_xml=models.FileField(upload_to=get_egret_loading_pattern_xml_path)
    
    class Meta:
        db_table='egret_input_xml'
        
        
        
    def __str__(self):
        return '{}'.format(self.unit)

def get_egret_upload_path(instance,filename):
    username=instance.user.get_username()
    cycle=instance.cycle
    unit=cycle.unit
    plant=unit.plant
    plant_name=plant.abbrEN
    name=os.path.basename(filename)
    task_name=instance.task_name
    return 'egret_task/{}/{}/unit{}/cycle{}/{}/{}'.format(username,plant_name,unit.unit, cycle.cycle,task_name,name) 

media_root=settings.MEDIA_ROOT



       
class EgretTask(BaseModel):
    task_name=models.CharField(max_length=32)
    cycle=models.ForeignKey('tragopan.Cycle')
    egret_input_file=models.FileField(upload_to=get_egret_upload_path,blank=True,null=True)
    follow_index=models.BooleanField()
    restart_file=models.FilePathField(path=media_root,recursive=True,blank=True,null=True)
    #depletion_composition=models.ManyToManyField('EgretDepletionCase')
    
    class Meta:
        db_table='egret_task'
        
        
        
    def __str__(self):
        return '{}'.format(self.task_name)
     
'''   
class EgretDepletionCase(models.Model):
    ralative_power=models.DecimalField(max_digits=6,decimal_places=5,validators=[MaxValueValidator(1.5),MinValueValidator(0)],help_text='0-1.5',)  
    burnup=models.DecimalField(max_digits=15,decimal_places=5,validators=[MinValueValidator(0),MaxValueValidator(100)],help_text='GWd/tU',blank=True,null=True)
    bank_position=models.CommaSeparatedIntegerField(max_length=100)
    delta_time=models.DecimalField(max_digits=10,decimal_places=3,validators=[MinValueValidator(0),],help_text='day',blank=True,null=True)
    SDC=models.BooleanField(default=False)
    
    class Meta:
        db_table='egret_depletion_case'
        
        
        
    def __str__(self):
        return '{}'.format(self.pk)
'''