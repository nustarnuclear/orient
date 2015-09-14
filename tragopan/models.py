from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


from django.db.models import Max




    
# base model to contain the basic information
class BaseModel(models.Model):
    time_inserted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    remark = models.TextField(blank=True)
    class Meta:
        abstract=True

#################################################       
# Concrete models in accordance with the database
#################################################

#################################################
#basic information 
#################################################

#describe element information
class Element(BaseModel):
    atomic_number = models.PositiveSmallIntegerField(primary_key=True)
    symbol = models.CharField(max_length=8,unique=True)
    nameCH = models.CharField(max_length=8)
    nameEN = models.CharField(max_length=40)
    reference = models.CharField(max_length=80, default='IUPAC')
    
    
    
    @staticmethod
    def autocomplete_search_fields():
        return ("atomic_number__iexact", "symbol__icontains",)
    
    class Meta:
        db_table='element'
        ordering=['atomic_number']
    def __str__(self):
        return self.symbol

    


class Nuclide(BaseModel):
    element = models.ForeignKey(Element,to_field="symbol",related_name='nuclides',related_query_name='nuclide')
    atom_mass = models.DecimalField(max_digits=9,decimal_places=6,validators=[MinValueValidator(0)])
    abundance = models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%")
    reference = models.CharField(max_length=80, default='IUPAC') 
   
    class Meta:
        db_table='Nuclide'
        unique_together = ('element', 'atom_mass')
        ordering=['element']
            
    def __str__(self):
        return "{}{}".format(self.element, round(self.atom_mass))
    
class WimsNuclideData(BaseModel):
    NF_CHOICES=(
                (0,'无共振积分表'),
                (1,'有共振积分表的非裂变核'),
                (2,'有共振吸收共振积分表的可裂变核'),
                (3,'有共振吸收和共振裂变共振积分表的可裂变核'),
                (4,'没有共振积分表的可裂变核'),
    )
    MATERIAL_TYPE_CHOICES=(
                           ('M','慢化剂'),
                           ('FP','裂变产物'),
                           ('A','锕系核素'),
                           ('B','可燃核素'),
                           ('D','用于剂量的材料'),
                           ('S','结构材料和其他'),
                           ('B/FP','可燃核素 /裂变产物'),
    )
    element = models.ForeignKey(Element,blank=True,null=True)
    nuclide_name= models.CharField(max_length=30,) 
    id_wims=models.PositiveIntegerField(unique=True)
    id_self_defined=models.PositiveIntegerField(unique=True,blank=True,null=True)
    amu= models.DecimalField(max_digits=9, decimal_places=6,validators=[MinValueValidator(0),])
    nf=models.PositiveSmallIntegerField(choices=NF_CHOICES)
    material_type= models.CharField(max_length=4,choices=MATERIAL_TYPE_CHOICES)
    descrip= models.CharField(max_length=50)
   
    @staticmethod
    def autocomplete_search_fields():
        return ("element__symbol",'id_wims')
    
    class Meta:
        db_table='wims_nuclide_data'
        
            
    def __str__(self):
        return "{}".format(self.nuclide_name)
  
class WmisElementData(BaseModel):
    element_name=models.CharField(max_length=30,)
    composition=models.ManyToManyField(WimsNuclideData,through='WmisElementComposition')
    
    @staticmethod
    def autocomplete_search_fields():
        return ("element_name__icontains",)
    
    class Meta:
        db_table='wmis_element_data'
        
    def __str__(self):
        return self.element_name
    
class WmisElementComposition(BaseModel):
    wmis_element=models.ForeignKey(WmisElementData,related_name='nuclides')
    wmis_nuclide=models.ForeignKey(WimsNuclideData)
    weight_percent=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%")
    
    class Meta:
        db_table='wmis_element_composition'
        
    def __str__(self):
        return '{} {}'.format(self.wmis_element, self.wmis_nuclide)

#describe material information
class Material(BaseModel):
    nameCH=models.CharField(max_length=40)
    nameEN=models.CharField(max_length=40)
    prerobin_identifier=models.CharField(max_length=20,blank=True)
    material_composition=models.ManyToManyField(WmisElementData,through='MaterialComposition')
    mixture_composition=models.ManyToManyField('self',symmetrical=False,through='MixtureComposition',through_fields=('mixture','material',))
    
    class Meta:
        db_table='Material'
        verbose_name='Material repository'
        verbose_name_plural='Material repository'
    
    def __str__(self):
        return self.nameEN
    
class MixtureComposition(BaseModel):
    mixture=models.ForeignKey(Material,related_name='mixtures',related_query_name='mixture')
    material=models.ForeignKey(Material)
    weight_percent=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%")
    
    class Meta:
        db_table='mixture_composition'
        
    def __str__(self):
        return "{} {}".format(self.mixture, self.material)
    
    
class MaterialComposition(BaseModel):
    material=models.ForeignKey(Material,related_name='elements',related_query_name='element')
    wims_element_data=models.ForeignKey(WmisElementData,blank=True,null=True,)
    weight_percent=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%",blank=True,null=True,)
    element_number=models.PositiveSmallIntegerField(blank=True,null=True)
    class Meta:
        db_table='material_composition'
        order_with_respect_to='material'
        
        
    
    def __str__(self):
        return '{} {}'.format(self.material, self.wims_element_data)
    
class MaterialAttribute(BaseModel):
    material=models.OneToOneField(Material,related_name='attribute')
    density=models.DecimalField(max_digits=15, decimal_places=5,help_text=r'unit:g/cm3')
    heat_capacity=models.DecimalField(max_digits=15, decimal_places=5,help_text=r'J/kg*K',blank=True,null=True)
    thermal_conductivity=models.DecimalField(max_digits=15, decimal_places=5,help_text=r'W/m*K',blank=True,null=True)
    expansion_coefficient=models.DecimalField(max_digits=15, decimal_places=5,help_text=r'm/K',blank=True,null=True)
    code = models.CharField(max_length=10, blank=True)
    class Meta:
        db_table='material_attribute'
        
    def __str__(self):
        return str(self.material)+"'s attribute"
    
#delete  MaterialNuclide model   
'''
class MaterialNuclide(BaseModel):
    'only describe the non natural element composition in material'
    material=models.ForeignKey(Material,related_name='nuclides',related_query_name='nuclide')
    nuclide=models.ForeignKey(Nuclide)
    weight_percent=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%")
    
    class Meta:
        db_table='material_nuclide'
    
    def __str__(self):
        return str(self.material)+' '+str(self.nuclide)
'''
    
class Vendor(BaseModel):
    TYPE_CHOICES=(
        ('Designer','Designer'),
        ('Manufacturer','Manufacturer'),
        ('Material','Material'),
    )
    nameCH=models.CharField(max_length=40)
    abbrCH=models.CharField(max_length=40)
    nameEN=models.CharField(max_length=40)
    abbrEN=models.CharField(max_length=40)
    type=models.CharField(max_length=12, choices=TYPE_CHOICES,default='Designer')
    
    class Meta:
        db_table='vendor'
        
    def __str__(self):
        return self.abbrCH
    
#################################################
#nuclear power plant basic information 
#################################################

class Plant(BaseModel):
    nameCH=models.CharField(max_length=40)
    abbrCH=models.CharField(max_length=40)
    nameEN=models.CharField(max_length=40)
    abbrEN=models.CharField(max_length=40)
    
    class Meta:
        db_table='plant'
        
    def __str__(self):
        return self.abbrEN  
    
class ReactorModel(BaseModel):
    MODEL_CHOICES=(
        ('QNPC2','QNPC2'),
        ('QNPC1','QNPC1'),
        ('M310','M310'),
        ('CAP1000','CAP1000'),
        ('AP1000','AP1000'),
    )
    GENERATION_CHOICES = (
        ('2', '2'),
        ('2+', '2+'),
        ('3', '3'),
    )

    TYPE_CHOICES = (
        ('PWR', 'PWR'),
        ('BWR', 'BWR'),
    )

    GEOMETRY_CHOICES = (
        ('Cartesian', 'Cartesian'),
        ('Hexagonal', 'Hexagonal'),
    )
    
    SYMBOL_CHOICES = (
        ('Number', 'Number'),
        ('Letter', 'Letter'),
    )


    name = models.CharField(max_length=50)
    generation = models.CharField(max_length=2, choices=GENERATION_CHOICES)
    reactor_type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    geometry_type = models.CharField(max_length=9, choices=GEOMETRY_CHOICES)
    row_symbol = models.CharField(max_length=6, choices=SYMBOL_CHOICES)
    column_symbol = models.CharField(max_length=6, choices=SYMBOL_CHOICES)
    num_loops = models.PositiveSmallIntegerField(blank=True,null=True)
    
    core_equivalent_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    active_height= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    cold_state_assembly_pitch= models.DecimalField(max_digits=7, decimal_places=4,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    hot_state_assembly_pitch = models.DecimalField(max_digits=7, decimal_places=4,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    vendor = models.ForeignKey(Vendor)  
    thermal_couple_position=models.ManyToManyField('ReactorPosition',related_name='thermal_couple_position',db_table='thermal_couple_map',blank=True,)
    incore_instrument_position=models.ManyToManyField('ReactorPosition',related_name='incore_instrument_position',db_table='incore_instrument_map',blank=True,)
   
    class Meta:
        db_table = 'reactor_model'
    
    def __str__(self):
        return '{}'.format(self.name)     

class ReactorPosition(BaseModel):
    reactor_model=models.ForeignKey(ReactorModel,related_name='positions',related_query_name='position')
    row=models.PositiveSmallIntegerField()
    column=models.PositiveSmallIntegerField()
    control_rod_mechanism=models.BooleanField(default=False,help_text='whether contain control rod mechanism',verbose_name='Whether can be inserted control rod assembly?')
    class Meta:
        db_table='reactor_position'
        unique_together=('reactor_model','row','column')
        ordering=['row','column']
        
    def __str__(self):
        rowSymbol=self.reactor_model.row_symbol
        columnSymbol=self.reactor_model.column_symbol
        #transform the number to letter
        if rowSymbol=='Letter' and columnSymbol=='Number':
            if self.row<=8:
                rowRpr=chr(self.row+64)
            else:
                rowRpr=chr(self.row+65)
            
            columnRpr=str(self.column).zfill(2)    
            return '{}{}'.format(rowRpr,columnRpr)    
        else:
            rowRpr=str(self.row).zfill(2)
            column_max=self.reactor_model.positions.aggregate(Max('column'))['column__max']
            index=66+column_max-self.column
            #kick 'Q'=81
            if index==80:
                columnRpr=chr(index+2)
            #kick 'O'=79
            elif index==79:
                columnRpr=chr(index+1)
            #kick 'I'
            elif index>73:
                columnRpr=chr(index)
            else:
                columnRpr=chr(index-1)
        
            return '{}{}'.format(columnRpr,rowRpr)

#################################################
#nuclear power plant equipment information
#################################################

class CoreBarrel(BaseModel):
    reactor_model =models.OneToOneField(ReactorModel)
    outer_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material = models.ForeignKey(Material)
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='core_barrel'
        
    def __str__(self):
        return "{}'s core barrel".format(self.reactor_model)
        
class CoreUpperPlate(BaseModel):
    reactor_model=models.OneToOneField(ReactorModel)
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:Kg')
    material = models.ForeignKey(Material)
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='core_upper_plate'
    
    def __str__(self):
        return "{}'s core upper plate".format(self.reactor_model)
    
class CoreLowerPlate(BaseModel):
    reactor_model=models.OneToOneField(ReactorModel)
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:Kg')
    material = models.ForeignKey(Material)
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='core_lower_plate'
    
    def __str__(self):
        return "{}'s core lower plate".format(self.reactor_model)
        
    
class ThermalShield(BaseModel):
    reactor_model=models.ForeignKey(ReactorModel)
    height =models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm') 
    outer_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    angle=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0),MaxValueValidator(360)],help_text='unit:degree')
    loc_height=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    loc_theta=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0),MaxValueValidator(360)],help_text='unit:degree')
    gap_to_barrel=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material = models.ForeignKey(Material)
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='thermal_shield'
    
    def __str__(self):
        return "{}'s {} thermal shield".format(self.reactor_model, self.id)
    
class PressureVessel(BaseModel):
    reactor_model=models.OneToOneField(ReactorModel)
    outer_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    weld_thickness = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    base_material = models.ForeignKey(Material,related_name='pressure_vessel_base')
    weld_material = models.ForeignKey(Material,related_name='pressure_vessel_weld')
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='pressure_vessel'
    
    def __str__(self):
        return "{}'s pressure vessel".format(self.reactor_model)

class PressureVesselInsulation(BaseModel):
    reactor_model=models.OneToOneField(ReactorModel)
    outer_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material = models.ForeignKey(Material)
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='pressure_vessel_insulation'
    
    def __str__(self):
        return "{}'s pressure vessel insulation".format(self.reactor_model)
    
class CoreBaffle(BaseModel):
    reactor_model=models.OneToOneField(ReactorModel)
    gap_to_fuel=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    outer_diameter=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material = models.ForeignKey(Material)
    thickness= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:Kg',blank=True,null=True)
    vendor = models.ForeignKey(Vendor)
    class Meta:
        db_table='core_baffle'
    
    def __str__(self):
        return "{}'s core baffle".format(self.reactor_model)

#rip plate table is associate with core baffle table    
class RipPlate(BaseModel):
    core_baffle=models.OneToOneField(ReactorModel)
    height=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    thickness=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    width= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    material = models.ForeignKey(Material)
    
    class Meta:
        db_table='rip_plate'
    
    def __str__(self):
        return "{}'s rip plate".format(self.core_baffle)


#################################################
#nuclear power plant operation information 
#################################################

class UnitParameter(BaseModel):
    plant = models.ForeignKey(Plant,related_name='units')
    unit = models.PositiveSmallIntegerField()
    reactor_model = models.ForeignKey(ReactorModel)
    electric_power = models.DecimalField(max_digits=10, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:MW')
    thermal_power = models.DecimalField(max_digits=10, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:MW')
    heat_fraction_in_fuel = models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%")
    primary_system_pressure= models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:MPa')
    ave_linear_power_density= models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text=r'unit:KW/m')
    ave_vol_power_density = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text=r'unit:KW/L', blank=True, null=True)
    ave_mass_power_density = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text=r'unit:KW/Kg (fuel)', blank=True, null=True)
    best_estimated_cool_vol_flow_rate = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text=r'unit:m3/h', blank=True, null=True)
    bypass_flow_fraction = models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%", blank=True, null=True)
    cold_state_cool_temp = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:K')
    HZP_cool_inlet_temp = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:K')
    HFP_cool_inlet_temp = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:K')
    HFP_core_ave_cool_temp = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:K', blank=True, null=True)
    mid_power_cool_inlet_temp = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:K', blank=True, null=True)
    
    class Meta:
        db_table = 'unit_parameter'
        unique_together = ('plant', 'unit')
    
    def __str__(self):
        return '{} U{}'.format(self.plant, self.unit)
 
class Cycle(BaseModel):
    unit=models.ForeignKey(UnitParameter)
    cycle = models.PositiveSmallIntegerField()
    starting_date = models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date',blank=True, null=True)
    shutdown_date = models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date',blank=True, null=True)
    cycle_length = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:EFPD',blank=True, null=True) 
    num_unplanned_shutdowns = models.PositiveSmallIntegerField(blank=True, null=True)
    num_periodical_tests = models.PositiveSmallIntegerField(blank=True, null=True)
    class Meta:
        db_table = 'cycle'
        unique_together = ('cycle', 'unit')
        verbose_name='Operation cycle'
        
    def __str__(self):
        return '{}C{}'.format(self.unit, self.cycle)
    
class FuelAssemblyLoadingPattern(BaseModel):
    ROTATION_DEGREE_CHOICES=(
        ('0','0'),
        ('90','90'),
        ('180','180'),
        ('270','270'),
    )
    cycle=models.ForeignKey(Cycle,related_name='fuel_assembly_loading_patterns')
    reactor_position=models.ForeignKey(ReactorPosition)
    fuel_assembly=models.ForeignKey('FuelAssemblyRepository',related_name='cycle_positions',default=1)
    
    following_index=models.CharField(max_length=60,blank=True, null=True)
    rotation_degree=models.CharField(max_length=3,choices=ROTATION_DEGREE_CHOICES,default='0')
    
    class Meta:
        db_table='fuel_assembly_loading_pattern'
       
        unique_together=(('cycle','reactor_position'),('cycle','fuel_assembly'))
        verbose_name='Incore fuel loading pattern'
    
    def get_previous(self):
        obj=FuelAssemblyLoadingPattern.objects.get(pk=self.pk)
        fuel_assembly=obj.fuel_assembly
        cycle=obj.cycle
        try:
            falp=FuelAssemblyLoadingPattern.objects.filter(fuel_assembly=fuel_assembly,cycle__cycle__lt=cycle.cycle,cycle__unit=cycle.unit).last()
            previous_cycle=falp.cycle
            previous_position=falp.reactor_position
            return "{}-{}-{}".format(previous_cycle.cycle,previous_position.row,previous_position.column)
        except:
            return None
        
    def get_grid(self):
        obj=FuelAssemblyLoadingPattern.objects.get(pk=self.pk)
        fuel_assembly=obj.fuel_assembly
        grids=fuel_assembly.type.model.grids.all()
        tmp_lst=[]
        for grid in grids:
            tmp=grid.grid.functionality+"("+str(grid.height)+")"
            tmp_lst.append(tmp)
        result='-'.join(tmp_lst)
        return result
        
       
    def __str__(self):
        return '{} {}'.format(self.cycle, self.reactor_position)


#################################################
#fuel assembly information 
#################################################  

class FuelAssemblyModel(BaseModel):
    name=models.CharField(max_length=20)
    overall_length=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    side_length=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    assembly_pitch=models.DecimalField(max_digits=7, decimal_places=4,validators=[MinValueValidator(0)],help_text='unit:cm')
    pin_pitch=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    lower_gap=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    upper_gap=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    licensed_max_discharge_BU =models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='MWd/tU',blank=True,null=True)
    licensed_pin_discharge_BU =models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='MWd/tU',blank=True,null=True)
    vendor=models.ForeignKey(Vendor)
    
    class Meta:
        db_table='fuel_assembly_model'
    
    def __str__(self):
        return "{}".format(self.name)

class FuelAssemblyType(BaseModel):
    model=models.ForeignKey(FuelAssemblyModel)
    assembly_enrichment=models.DecimalField(max_digits=4, decimal_places=3,validators=[MinValueValidator(0)],help_text='meaningful only if using the one unique enrichment fuel',blank=True,null=True)
    fuel_element_Type_position=models.ManyToManyField('FuelElementType',through='FuelElementTypePosition')
    
    class Meta:
        db_table='fuel_assembly_type'
        
    def __str__(self):
        obj=FuelAssemblyType.objects.get(pk=self.pk)
        if  obj.positions.all().first():
            fe=obj.positions.all().first().fuel_element_type
            fp=fe.fuel_pellet_map.all().first().fuel_pellet_type
            mt=fp.material
            
        else:
            mt=''
        return "{} {} {}".format(self.pk,self.model,mt)  
    

    
class FuelAssemblyRepository(BaseModel):
    PN=models.CharField(max_length=50,unique=True,blank=True,null=True)
    type=models.ForeignKey(FuelAssemblyType)
    batch_number=models.PositiveSmallIntegerField(blank=True,null=True)
    manufacturing_date=models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date',blank=True,null=True)
    arrival_date=models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date',blank=True,null=True)
    plant=models.ForeignKey(Plant)
    vendor=models.ForeignKey(Vendor,default=1)
    availability=models.BooleanField(default=True)
    class Meta:
        db_table='fuel_assembly_repository'
        verbose_name_plural='Fuel assembly repository'
    def __str__(self):
        return "{} {}".format(self.pk, self.type)
    
    
#the position information of fuel assembly     
class FuelAssemblyPosition(BaseModel):
    TYPE_CHOICES=(('fuel','fuel element tube'),
                  ('guide','guide tube'),
                  ('instrument','instrument tube'),
                  )
    fuel_assembly_model=models.ForeignKey(FuelAssemblyModel,related_name='positions',related_query_name='position')
    row=models.PositiveSmallIntegerField()
    column=models.PositiveSmallIntegerField()
    type=models.CharField(max_length=10,choices=TYPE_CHOICES,default='fuel')
    
    class Meta:
        db_table='fuel_assembly_position'
        unique_together=('fuel_assembly_model','row','column')
        verbose_name='Intra-assembly rod pattern'
    def __str__(self):
        return '{} R{}C{}'.format(self.fuel_assembly_model, self.row,self.column)

class FuelElementTypePosition(BaseModel):
    fuel_assembly_type=models.ForeignKey(FuelAssemblyType,related_name='positions',related_query_name='position')
    fuel_assembly_position=models.ForeignKey(FuelAssemblyPosition,limit_choices_to={'type': 'fuel'})
    fuel_element_type=models.ForeignKey('FuelElementType')
    
    class Meta:
        db_table='fuel_element_type_position'
        unique_together=('fuel_assembly_type','fuel_assembly_position')
        verbose_name='Intra-assembly fuel element loading pattern'
    
    def __str__(self):
        return '{} {}'.format(self.fuel_element_type,self.fuel_assembly_position)
    



class GridPosition(BaseModel):
    fuel_assembly_model=models.ForeignKey(FuelAssemblyModel,related_name='grids')
    grid=models.ForeignKey('Grid')
    height= models.DecimalField(max_digits=10, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm Base on bottom of fuel') 
    
    class Meta:
        db_table='grid_position'
        
    def __str__(self):
        return '{} {}'.format(self.fuel_assembly_model, self.grid)    

#the component of fuel assembly
class Grid(BaseModel):
    FUCTIONALITY_CHOICS=(
                ('blend','blend'),
                ('fix','fix'),
    )
    name=models.CharField(max_length=50)
    fuel_assembly_model=models.ForeignKey(FuelAssemblyModel,related_name='fuel_assembly_grids')
    side_length=models.DecimalField(max_digits=10, decimal_places=5,validators=[MinValueValidator(0)],help_text='cm')

    
    sleeve_height=models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='cm')
    inner_sleeve_thickness=models.DecimalField(max_digits=10, decimal_places=5,validators=[MinValueValidator(0)],help_text='cm')
    outer_sleeve_thickness=models.DecimalField(max_digits=10, decimal_places=5,validators=[MinValueValidator(0)],help_text='cm')
    sleeve_material=models.ForeignKey(Material,related_name='grid_sleeves',related_query_name='grid_sleeve',blank=True,null=True)
    
    spring_thickness=models.DecimalField(max_digits=10, decimal_places=5,validators=[MinValueValidator(0)],help_text='cm',blank=True,null=True)
    spring_material=models.ForeignKey(Material,related_name='grid_springs',related_query_name='grid_spring',blank=True,null=True)
    functionality=models.CharField(max_length=5,choices=FUCTIONALITY_CHOICS,default='fix')
    
    
    class Meta:
        db_table='grid'
        verbose_name='Fuel grid'
    
    def __str__(self):
        return '{} {}'.format(self.fuel_assembly_model,self.name)

  
class GuideTube(BaseModel):
    fuel_assembly_model=models.OneToOneField(FuelAssemblyModel)
    upper_outer_diameter= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    upper_inner_diameter= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    buffer_outer_diameter=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm',null=True)
    buffer_inner_diameter=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm',null=True)
    material=models.ForeignKey(Material)
    
    
    class Meta:
        db_table='guide_tube'
        
    def __str__(self):
        return "{} guid tube".format(self.material)
    
class InstrumentTube(BaseModel):
    fuel_assembly_model=models.OneToOneField(FuelAssemblyModel)
    outer_diameter= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material=models.ForeignKey(Material)
    
    
    class Meta:
        db_table='instrument_tube'
        
    def __str__(self):
        return "{}'s instrument tube".format(self.material)
    
class UpperNozzle(BaseModel):
    fuel_assembly_model=models.OneToOneField(FuelAssemblyModel)
    pitch=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    plate_thickness=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    plate_porosity=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%")
    height=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material=models.ForeignKey(Material)
    
    
    class Meta:
        db_table='upper_nozzle'
        
    def __str__(self):
        return "{}'s upper nozzle".format(self.fuel_assembly_model)
    
class LowerNozzle(BaseModel):
    fuel_assembly_model=models.OneToOneField(FuelAssemblyModel)
    pitch=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    plate_thickness=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    plate_porosity=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%")
    height=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material=models.ForeignKey(Material)
    
    
    class Meta:
        db_table='lower_nozzle'
        
    def __str__(self):
        return "{}'s lower nozzle".format(self.fuel_assembly_model)
    
#################################################
#fuel element information 
################################################# 

class FuelElement(BaseModel):
    fuel_assembly_model=models.OneToOneField(FuelAssemblyModel)
    overall_length=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    active_length=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    plenum_length=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    filling_gas_pressure=models.DecimalField(max_digits=10, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:MPa',blank=True,null=True)
    filling_gas_material=models.ForeignKey(Material,blank=True,null=True)
    
    
    class Meta:
        db_table='fuel_element'
        
    def __str__(self):
        return "{} fuel element".format(self.fuel_assembly_model)

class FuelElementType(BaseModel):
    model=models.ForeignKey(FuelElement)
    pellet=models.ManyToManyField('FuelPelletType',through='FuelElementPelletLoadingScheme')
    
    class Meta:
        db_table='fuel_element_type'
        
    def __str__(self):
        obj=FuelElementType.objects.get(pk=self.pk)
        ctr=obj.fuel_pellet_map.all().first()
        if  ctr:
            fp=ctr.fuel_pellet_type
            mt=fp.material
            
        else:
            mt=''
        
        return "{} {} {}".format(self.pk,self.model,mt)
    
    
class UpperCap(BaseModel):
    fuel_element_type=models.OneToOneField(FuelElement)
    height=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material=models.ForeignKey(Material)
  
    
    class Meta:
        db_table='upper_cap'
        
    def __str__(self):
        return "{}'s upper cap".format(self.fuel_element_type)
    

class LowerCap(BaseModel):
    fuel_element=models.OneToOneField(FuelElement)
    height=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material=models.ForeignKey(Material)
    
    
    class Meta:
        db_table='lower_cap'
        
    def __str__(self):
        return "{}'s lower cap".format(self.fuel_element)
    
class PlenumSpring(BaseModel):
    fuel_element=models.OneToOneField(FuelElement)
    weight=models.DecimalField(max_digits=10, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:g')
    outer_diameter= models.DecimalField(max_digits=7, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm')
    wire_diameter=models.DecimalField(max_digits=7, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm')
    material=models.ForeignKey(Material)
    
    
    class Meta:
        db_table='plenum_spring'
        
    def __str__(self):
        return "{}'s plenum spring".format(self.fuel_element)
    
class CladdingTube(BaseModel):
    fuel_element=models.OneToOneField(FuelElement)
    outer_diameter= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    roughness= models.DecimalField(max_digits=7, decimal_places=6,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    material=models.ForeignKey(Material)
    
    
    class Meta:
        db_table='cladding_tube'
        
    def __str__(self):
        return "{}'s cladding tube".format(self.fuel_element)
    

#fake fuel element information 
class FakeFuelElementType(BaseModel):
    fuel_assembly_model=models.OneToOneField(FuelAssemblyModel)
    overall_length=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    outer_diameter=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    pellet_outer_diameter=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    pellet_height=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material=models.ForeignKey(Material)
    
    class Meta:
        db_table='fake_fuel_element_type'
        
    def __str__(self):
        return '{} fake fuel element'.format(self.material)
    


#Fuel Pellet 
class FuelPellet(BaseModel):
    fuel_assembly_model=models.OneToOneField(FuelAssemblyModel)
    outer_diameter=models.DecimalField(max_digits=7, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter=models.DecimalField(max_digits=7, decimal_places=5,validators=[MinValueValidator(0)],blank=True,null=True,help_text='unit:cm can be none when hollow')
    length=models.DecimalField(max_digits=7, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm')
    dish_volume_percentage=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%",blank=True,null=True)
    chamfer_volume_percentage=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%",blank=True,null=True)
    dish_depth=models.DecimalField(max_digits=7, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    dish_diameter=models.DecimalField(max_digits=7, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    roughness=models.DecimalField(max_digits=7, decimal_places=6,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    nominal_density=models.DecimalField(max_digits=8, decimal_places=5,validators=[MinValueValidator(0)],help_text=r"unit:g/cm3")
    uncertainty_percentage=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%",blank=True,null=True)  
    coating_thickness=models.DecimalField(max_digits=7, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    coating_material=models.ForeignKey(Material,related_name='fuel_pellet_coating',blank=True,null=True)
    
    class Meta:
        db_table='fuel_pellet'
        
    def __str__(self):
        return '{} pellet'.format(self.fuel_assembly_model)

class FuelPelletType(BaseModel):
    model=models.ForeignKey(FuelPellet)
    material=models.ForeignKey(Material,related_name='fuel_pellet_material')
    
    class Meta:
        db_table='fuel_pellet_type'
        
    def __str__(self):
        return '{} {} {}'.format(self.pk,self.model,self.material)
    
    
class FuelElementPelletLoadingScheme(BaseModel):
    fuel_element_type=models.ForeignKey(FuelElementType,related_name='fuel_pellet_map')
    fuel_pellet_type=models.ForeignKey(FuelPelletType)
    section=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm height base on bottom')
    
    class Meta:
        db_table='fuel_element_pellet_loading_scheme'
        
    def __str__(self):
        return '{} {} {}'.format(self.fuel_element_type, self.section,self.fuel_pellet_type)
    

    
#################################################
#component assembly information 
#################################################    

####################################################################################################################################
#the following five models describe all the component rod type
class ControlRodType(BaseModel):
    fuel_assembly_model=models.ForeignKey(FuelAssemblyModel)
    absorb_material=models.ForeignKey(Material,related_name='control_rod_absorb')
    absorb_length=models.DecimalField(max_digits=9, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm')
    absorb_diameter=models.DecimalField(max_digits=7, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm')
    cladding_material=models.ForeignKey(Material,related_name='control_rod_cladding')
    cladding_inner_diameter=models.DecimalField(max_digits=7, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm')
    cladding_outer_diameter=models.DecimalField(max_digits=7, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm')
    
    class Meta:
        db_table='control_rod_type'
        verbose_name='Control rod'
        
    def __str__(self):
        return '{} control rod'.format(self.fuel_assembly_model)
    
class SourceRodType(BaseModel):
    fuel_assembly_model=models.ForeignKey(FuelAssemblyModel)
    TYPE_CHOICES=(
                  ('primary','primary'),
                  ('secondary','secondary')
    )
    type=models.CharField(max_length=9,choices=TYPE_CHOICES)
    overall_length=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    diameter=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    material=models.ForeignKey(Material,blank=True,null=True)
    strength=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:10e8')
    
    class Meta:
        db_table='source_rod_type'
    
    def __str__(self):
        return '{} {}'.format(self.type, self.fuel_assembly_model)

class NozzlePlugRod(BaseModel):
    fuel_assembly_model=models.OneToOneField(FuelAssemblyModel)
    length=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    diameter=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material=models.ForeignKey(Material)
    
    class Meta:
        db_table='nozzle_plug_rod'
    
    def __str__(self):
        return '{} nozzle plug rod'.format(self.material)
    
class BurnablePoisonRod(BaseModel):
    fuel_assembly_model=models.OneToOneField(FuelAssemblyModel)
    length=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    active_length=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')                   
    radial_map=models.ManyToManyField(Material,through='BurnablePoisonMaterial',related_name='burnable_poison_rod')
    
    class Meta:
        db_table='burnable_poison_rod'
        verbose_name='Burnable absorber rod'
    
    def __str__(self):
        return '{} burnable poison rod'.format(self.fuel_assembly_model)
    
    
class BurnablePoisonMaterial(BaseModel):
    burnable_poison_rod=models.ForeignKey(BurnablePoisonRod)
    material=models.ForeignKey(Material)
    radius=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    
    class Meta:
        db_table='burnable_poison_rod_material'
        
    def __str__(self):
        return '{} {}'.format(self.burnable_poison_rod,self.material)
######################################################################################################################
    
    

############################################################################
#the following three tables combine to describe burnable poison assembly   
class BurnablePoisonAssembly(BaseModel):
    fuel_assembly_model=models.ForeignKey(FuelAssemblyModel)
    burnable_poison_map=models.ManyToManyField(FuelAssemblyPosition,through='BurnablePoisonRodMap',related_name='bp_burnable_poison')
    
    
    class Meta:
        db_table='burnable_poison_assembly'
        verbose_name='Burnable absorber rod pattern'
        
    def get_poison_rod_num(self):
        obj=BurnablePoisonAssembly.objects.get(pk=self.pk)
        num=obj.rod_positions.count()
        return num  
    def get_poison_rod_height(self): 
        obj=BurnablePoisonAssembly.objects.get(pk=self.pk)
        height=obj.rod_positions.first().height
        return height
    def __str__(self):
        obj=BurnablePoisonAssembly.objects.get(pk=self.pk)
        num=obj.rod_positions.count()
        return '{} {}'.format(num, self.fuel_assembly_model)
    
    
class BurnablePoisonRodMap(BaseModel):
    burnable_poison_assembly=models.ForeignKey(BurnablePoisonAssembly,related_name='rod_positions')
    burnable_poison_position=models.ForeignKey(FuelAssemblyPosition,limit_choices_to={'type':'guide'})
    height=models.DecimalField(max_digits=7, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:cm')
   

    
    class Meta:
        db_table='burnable_poison_rod_map'
        unique_together=('burnable_poison_assembly','burnable_poison_position')
    def __str__(self):
        return '{}'.format(self.burnable_poison_assembly)
    
class BurnablePoisonAssemblyLoadingPattern(BaseModel):
    
    cycle=models.ForeignKey(Cycle,related_name='burnable_posison_assembly_positions')
    reactor_position=models.ForeignKey(ReactorPosition)
    burnable_poison_assembly=models.ForeignKey(BurnablePoisonAssembly)
    
    

    class Meta:
        db_table='burnable_poison_assembly_loading_pattern'
        
        unique_together=('reactor_position','burnable_poison_assembly')
        verbose_name='Burnable absorber assembly'
        verbose_name_plural='Burnable absorber assemblies'
    
    def __str__(self):
        return '{} {}'.format(self.cycle, self.reactor_position)
    
    
    
###############################################################################
#the following two models describe control rod assembly
class ControlRodAssembly(BaseModel):
    TYPE_CHOICES=(
                  ('shutdown','shutdown'),
                  ('adjust','adjust'),
    )
    cluster_name=models.CharField(max_length=5)
    type=models.CharField(max_length=8,choices=TYPE_CHOICES)
    fuel_assembly_model=models.ForeignKey(FuelAssemblyModel)
    primary=models.BooleanField(default=False,verbose_name='if primary?')
    control_rod_map=models.ManyToManyField(FuelAssemblyPosition,through='ControlRodMap')
    
    class Meta:
        db_table='control_rod_assembly'
       
        verbose_name_plural='Control rod assemblies'
        
    def __str__(self):
        return '{} {} control cluster'.format(self.fuel_assembly_model,self.cluster_name)
    
class ControlRodMap(BaseModel):
    control_rod_assembly=models.ForeignKey(ControlRodAssembly,related_name='control_rods')
    guide_tube_position=models.ForeignKey(FuelAssemblyPosition,limit_choices_to={'type': 'guide'})
    control_rod_type=models.ForeignKey(ControlRodType)
    
    
    class Meta:
        db_table='control_rod_map'
        unique_together=('control_rod_assembly','guide_tube_position')
    def __str__(self):
        return '{} {}'.format(self.control_rod_assembly,self.control_rod_type)
    
class ControlRodAssemblyLoadingPattern(BaseModel):
   
    reactor_position=models.ForeignKey(ReactorPosition,limit_choices_to={'control_rod_mechanism':True})
    control_rod_assembly=models.ForeignKey(ControlRodAssembly)
    
    

    class Meta:
        db_table='control_rod_assembly_loading_pattern'
        
     
        
    
    def __str__(self):
        return '{} '.format(self.reactor_position)    
    

##############################################################################
#the following four models combine to describe source assembly 
class SourceAssembly(BaseModel):
    fuel_assembly_model=models.ForeignKey(FuelAssemblyModel)
    source_rod_map=models.ManyToManyField(FuelAssemblyPosition,through='SourceRodMap')
    
    
    
    class Meta:
        db_table='source_assembly' 
        verbose_name_plural='Source assemblies'   
        
    def __str__(self):
        obj=SourceAssembly.objects.get(pk=self.pk)
        num=obj.source_rod_positions.filter(source_rod__type='primary').count()    
        if num:
            name='primary'
        else:
            name='secondary'
       
        return '{} {} source assembly'.format(self.fuel_assembly_model,name)
    
class SourceRodMap(BaseModel):
    source_assembly=models.ForeignKey(SourceAssembly,related_name='source_rod_positions')
    source_rod_position=models.ForeignKey(FuelAssemblyPosition,limit_choices_to={'type': 'guide'})
    source_rod=models.ForeignKey(SourceRodType)
    
    class Meta:
        db_table='source_rod_map'
    
    def __str__(self):
        return '{} {}'.format(self.source_assembly, self.source_rod_position)


class SourceAssemblyLoadingPattern(BaseModel):
    cycle=models.ForeignKey(Cycle,related_name='source_assembly_positions')
    reactor_position=models.ForeignKey(ReactorPosition)
    source_assembly=models.ForeignKey(SourceAssembly)
    
    

    class Meta:
        db_table='source_assembly_loading_pattern'
        unique_together=('cycle','reactor_position')
        
    
    def __str__(self):
        return '{} {}'.format(self.cycle, self.reactor_position)  
    
    
    
    
################################################################################ 
#the following 2 models describe nozzle plug assembly

class NozzlePlugAssembly(BaseModel):
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:Kg')
    nozzle_plug_rod=models.ManyToManyField(NozzlePlugRod,through='NozzlePlugRodMap')
    
    class Meta:
        db_table='nozzle_plug_assembly'
        verbose_name_plural='Nozzle plug assemblies'
    
    def __str__(self):
        return '{}'.format(self.weight) 

class NozzlePlugRodMap(BaseModel):
    nozzle_plug_assembly=models.ForeignKey(NozzlePlugAssembly)
    guid_tube_position=models.OneToOneField(FuelAssemblyPosition,limit_choices_to={'type': 'guide'})
    nozzle_plug_rod=models.ForeignKey(NozzlePlugRod)
    
    class Meta:
        db_table='nozzle_plug_rod_map'
        
    def __str__(self):
        return '{} {}'.format(self.nozzle_plug_assembly, self.nozzle_plug_rod)
    
 
class OperationParameter(BaseModel):
    unit=models.ForeignKey(UnitParameter)
    date=models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date',blank=True,null=True) 
    burnup=models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:MWd/tU')
    nuclear_power=models.DecimalField(max_digits=10, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:MW')
    theoretical_boron_density=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:ppm')
    measured_boron_density=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:ppm')
    coolant_average_temperature=models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:K')
    axial_power_shift=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(-100)],help_text=r"unit:%FP")
    control_rod_step=models.ManyToManyField(ControlRodAssembly,through='ControlRodAssemblyStep')
    
    class Meta:
        db_table='operation_parameter'
        
    def __str__(self):
        return '{} {}'.format(self.unit, self.date)  
    
class ControlRodAssemblyStep(BaseModel):
    operation=models.ForeignKey(OperationParameter)
    control_rod_assembly=models.ForeignKey(ControlRodAssembly)
    step=models.PositiveSmallIntegerField()
    
    class Meta:
        db_table='control_rod_assembly_step'
        
    def __str__(self):
        return '{} {}'.format(self.control_rod_assembly, self.step)



        

        
    

    
    
    
    
