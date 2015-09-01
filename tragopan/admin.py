from django.contrib import admin
from .models import *
from django.db.models import Sum,F,Count
from .forms import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

#################################################
#basic information 
#################################################

#element information

class NuclideInline(admin.TabularInline):
    model=Nuclide
    extra=0
    exclude=('reference','remark')
    #list_display=('__str__','atom_mass','abundance',)
    readonly_fields=('atom_mass','abundance')
    

class ElementResource(resources.ModelResource):

    class Meta:
        model = Element
        fields = ('atomic_number', 'symbol', 'nameCH','nameEN','reference')
        
        
class ElementAdmin(ImportExportModelAdmin):
    resource_class = ElementResource
    
    fieldsets=[
               (None,{'fields':['atomic_number','symbol']}),
               ('Element information',{'fields':['nameCH','nameEN'],'classes': ['collapse']})
             ]
    inlines=[NuclideInline]
    search_fields=('=symbol',)
    readonly_fields=('atomic_number','symbol','nameCH','nameEN')
    list_display=('atomic_number','symbol','nameCH','nameEN','element_average_mass','get_isotopes_num','is_correct',)
    list_display_links=('atomic_number','symbol','nameCH','nameEN')
    
    #calculate the average mass of each element
    def element_average_mass(self,obj):
        element_mass=obj.nuclides.all().aggregate(avg_mass=Sum(F('atom_mass')*F('abundance')/100))
        if element_mass['avg_mass']==0:
            return 'Non Existent in nature'
        return str(round(element_mass['avg_mass'],5))       
    element_average_mass.short_description='Element Mass'
    
    #get the natural existent isotopes number of each element
    def get_isotopes_num(self,obj):
        isotopes=obj.nuclides.filter(abundance__gt=0).aggregate(num_isotopes=Count('id'))
        return isotopes['num_isotopes']
    get_isotopes_num.short_description='Natural Existent Isotopes Count'
    
    #check if satisfy the integrity constraint
    def is_correct(self,obj):
        pecentage_sum=obj.nuclides.all().aggregate(sum=Sum('abundance'))
        if pecentage_sum['sum'] in [100,0]:
            return True
        return False
    is_correct.short_description='Data Integrity?'
    is_correct.boolean=True       
admin.site.register(Element, ElementAdmin)

class NuclideAdmin(admin.ModelAdmin):
    exclude=('reference','remark')
    search_fields=('=element__symbol',)
    ordering=('element','atom_mass')
    list_display=('__str__','atom_mass','abundance')
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('element','atom_mass','abundance')
        return ()    
    
    # define the raw_id_fields
    #raw_id_fields = ('element',)
    # define the autocomplete_lookup_fields
    #autocomplete_lookup_fields = {
    #    'fk': ['element'],
    #}
admin.site.register(Nuclide, NuclideAdmin)

class WimsNuclideDataAdmin(admin.ModelAdmin):
    list_display=('__str__','element','id_wims','id_self_defined','amu','nf','material_type','descrip')
    #list_editable=('id_self_defined',)
    ordering=('time_inserted',)
    list_filter=('element','id_wims','nf','material_type')
    search_fields=('=id_wims','=element__symbol',)
    raw_id_fields = ('element',)
    autocomplete_lookup_fields = {
        'fk': ['element',],
    }
admin.site.register(WimsNuclideData, WimsNuclideDataAdmin)   

class WmisElementCompositionInline(admin.TabularInline):
    model=WmisElementComposition
    exclude=('remark',)
    extra=0

class WmisElementDataAdmin(admin.ModelAdmin):
    ordering=('time_inserted',)
    exclude=('remark',)
    inlines=[WmisElementCompositionInline,]
    list_display=('__str__','is_correct',)
    #check if satisfy the integrity constraint
    def is_correct(self,obj):
        cps=obj.nuclides.all()
        pecentage_sum=0
        for cp in cps:
            pecentage_sum +=cp.weight_percent
            
        if pecentage_sum==100:
            return True
        return False
    is_correct.short_description='Data Integrity?'
    is_correct.boolean=True  
    
admin.site.register(WmisElementData, WmisElementDataAdmin) 


#material information
class MaterialCompositionInline(admin.TabularInline):
    model=MaterialComposition
    exclude=('remark',)
    raw_id_fields = ('wims_element_data',)
    # define the related_lookup_fields
    autocomplete_lookup_fields = {
        'fk': ['wims_element_data',],
    }
    related_lookup_fields = {
        'fk': ['wims_element_data',],
        
    }
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra-1
        return extra
  
#mixture information
class MixtureCompositionInline(admin.TabularInline):
    model=MixtureComposition
    exclude=('remark',)
    fk_name='mixture'
    extra=0


class MaterialAttributeInline(admin.TabularInline):
    model=MaterialAttribute
    extra=1
    exclude=('remark',)
    
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('density','heat_capacity','thermal_conductivity','expansion_coefficient','code')

        return ()

    
class MaterialAdmin(admin.ModelAdmin):
    inlines=(MaterialCompositionInline,MaterialAttributeInline,MixtureCompositionInline)
    exclude=('remark',)
    list_display=('nameEN','nameCH','prerobin_identifier','is_correct')
    list_display_links=('nameEN','nameCH')
    list_editable=('prerobin_identifier',)
    
    #check if satisfy the integrity constraint
    def is_correct(self,obj):
        if obj.elements.all().first():
            if obj.elements.all().first().weight_percent:
                pecentage_sum=obj.elements.all().aggregate(sum=Sum('weight_percent'))
                if pecentage_sum['sum']==100:
                    return True
                return False
        return True
    is_correct.short_description='Data Integrity?'
    is_correct.boolean=True
    
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('nameEN','nameCH')
        return ()
admin.site.register(Material, MaterialAdmin)

class VendorAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_display=('nameEN','nameCH','type')
    list_display_links=('nameEN','nameCH')
    
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('nameCH','nameEN','abbrCH','abbrEN','type')
        return ()
admin.site.register(Vendor, VendorAdmin)

#################################################
#nuclear power plant basic information 
#################################################
class UnitParameterInline(admin.TabularInline):
    model=UnitParameter
    exclude=('remark',)
    extra=0
    #show_change_link=True


class PlantResource(resources.ModelResource):

    class Meta:
        model = Plant
        fields=('id','nameCH','abbrCH','nameEN','abbrEN',)
        
class PlantAdmin(ImportExportModelAdmin):
    resource_class = PlantResource
    
    exclude=('remark',)
    list_display=('nameEN','nameCH','get_unit_num')
    list_display_links=('nameEN','nameCH')
    inlines=(UnitParameterInline,)
    
    #def get_readonly_fields(self,request, obj=None):
    #    if not request.user.is_superuser:
    #        return ('nameCH','nameEN','abbrCH','abbrEN')
    #    return ()
    
    def get_unit_num(self,obj):
        unit_num=obj.units.count()
        return unit_num
    get_unit_num.short_description='unit number'
admin.site.register(Plant, PlantAdmin)

class ReactorPositionAdmin(admin.ModelAdmin):
    exclude=('remark',)
    search_fields=('=row','=column')
    list_filter=('reactor_model__name',)
    list_display=('reactor_model','__str__','control_rod_mechanism')
    list_editable=('control_rod_mechanism',)
    list_per_page=200
    ordering=('row','column')
    
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('reactor_model','row','column')
        return ()
admin.site.register(ReactorPosition, ReactorPositionAdmin)

#the following inline tables describe a kind of reactor model
class ReactorPositionInline(admin.TabularInline):
    model=ReactorPosition
    exclude=('remark',)
    
    def get_extra(self, request, obj=None, **kwargs):
        extra = 121
        if obj:
            extra -= obj.positions.count()
        return extra
    
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('row','column',)
        return ()

class CoreBarrelInline(admin.TabularInline):
    model=CoreBarrel
    extra=1
    exclude=('remark',)
    verbose_name_plural='core barrel'
    
class CoreUpperPlateInline(admin.TabularInline):
    model=CoreUpperPlate
    extra=1
    exclude=('remark',)
    verbose_name_plural='core upper plate'
    
class CoreLowerPlateInline(admin.TabularInline):
    model=CoreLowerPlate
    extra=1
    exclude=('remark',)
    verbose_name_plural='core lower plate'
    
class ThermalShieldInline(admin.TabularInline):
    model=ThermalShield
    extra=1
    exclude=('remark',)

class PressureVesselInline(admin.TabularInline):
    model=PressureVessel
    extra=1
    exclude=('remark',)
    verbose_name_plural='pressure vessel'
    
class PressureVesselInsulationInline(admin.TabularInline):
    model=PressureVesselInsulation
    extra=1
    exclude=('remark',)
    verbose_name_plural='pressure vessel insulation'
    
class CoreBaffleInline(admin.TabularInline):
    model=CoreBaffle
    extra=1
    exclude=('remark',)
    verbose_name_plural='core baffle'

class ThermalCouplePositionInline(admin.TabularInline):
    model = ReactorModel.thermal_couple_position.through
    verbose_name='thermal_couple_position'
    verbose_name_plural='thermal couple position'
    
    def get_extra(self, request, obj=None, **kwargs):
        extra =30
        if obj:
            extra -= obj.thermal_couple_position.count()
        return extra
    

class IncoreInstrumentPositionInline(admin.TabularInline):
    model = ReactorModel.incore_instrument_position.through
    verbose_name='incore_instrument_position'
    verbose_name_plural='incore instrument position'
    
    def get_extra(self, request, obj=None, **kwargs):
        extra =38
        if obj:
            extra -= obj.incore_instrument_position.count()
        return extra
    
class ReactorModelAdmin(admin.ModelAdmin):
    exclude=('remark','thermal_couple_position','incore_instrument_position')
    inlines=[CoreBaffleInline,CoreUpperPlateInline,CoreLowerPlateInline,ThermalShieldInline,PressureVesselInline,PressureVesselInsulationInline,CoreBaffleInline,
             ]
    #raw_id_fields=('thermal_couple_position','incore_instrument_position')
    list_display=['name','generation','reactor_type','geometry_type','num_loops',
                  'get_thermal_couple_num','get_incore_instrument_num','get_fuel_assembly_num','get_control_rod_mechanism_num']
    
    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if not request.user.is_superuser:
                if isinstance(inline, ThermalCouplePositionInline) or isinstance(inline, IncoreInstrumentPositionInline):
                    continue
            yield inline.get_formset(request, obj), inline
    
    def get_thermal_couple_num(self,obj):
        num=obj.thermal_couple_position.count()
        return num
    get_thermal_couple_num.short_description='thermal couple count'
    
    def get_incore_instrument_num(self,obj):
        num=obj.incore_instrument_position.count()
        return num
    get_incore_instrument_num.short_description='incore instrument count'
    
    def get_control_rod_mechanism_num(self,obj):
        num=obj.positions.filter(control_rod_mechanism=True).count()
        return num
    get_control_rod_mechanism_num.short_description='control rod mechanism count'
    
    def get_fuel_assembly_num(self,obj):
        num=obj.positions.count()
        return num
    get_fuel_assembly_num.short_description='fuel assembly count'
    
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('model','generation','reactor_type','geometry_type','row_symbol','column_symbol',
                    'num_loops','num_control_rod_mechanisms','core_equivalent_diameter','active_height','cold_state_assembly_pitch','hot_state_assembly_pitch','vendor','thermal_couple_position','incore_instrument_position')
        return ()
      
admin.site.register(ReactorModel,ReactorModelAdmin)

class UnitParameterAdmin(admin.ModelAdmin):
    exclude=('remark',)
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('plant','unit','reactor_model','electric_power','thermal_power','heat_fraction_in_fuel','primary_system_pressure',
                    'ave_linear_power_density','ave_vol_power_density','ave_mass_power_density','best_estimated_cool_vol_flow_rate','bypass_flow_fraction',
                    'cold_state_cool_temp','HZP_cool_inlet_temp','HFP_cool_inlet_temp','HFP_core_ave_cool_temp','mid_power_cool_inlet_temp',)
        return ()
admin.site.register(UnitParameter, UnitParameterAdmin)

#plant operation information
class FuelAssemblyLoadingPatternInline(admin.TabularInline):
    exclude=('remark',)
    model=FuelAssemblyLoadingPattern
    extra=0
    raw_id_fields = ("fuel_assembly",)

class FuelAssemblyLoadingPatternAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_filter=['fuel_assembly','reactor_position','cycle']
    list_display=['cycle','reactor_position','fuel_assembly','get_previous']
    
    raw_id_fields = ("fuel_assembly",)
    ordering=('cycle','reactor_position')
    list_editable=("fuel_assembly",)
    list_per_page=121
admin.site.register(FuelAssemblyLoadingPattern, FuelAssemblyLoadingPatternAdmin)


class BurnablePoisonAssemblyLoadingPatternInline(admin.TabularInline):
    exclude=('remark',)
    extra=0
    model=BurnablePoisonAssemblyLoadingPattern    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "reactor_position":
            try:
                kwargs["queryset"] = ReactorPosition.objects.filter(reactor_model=Cycle.objects.get(pk=int(request.path.split(sep='/')[-2])).unit.reactor_model)
            except Exception:
                pass
        return super(BurnablePoisonAssemblyLoadingPatternInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

class SourceAssemblyLoadingPatternInline(admin.TabularInline):
    exclude=('remark',)
    extra=0
    model=SourceAssemblyLoadingPattern
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "reactor_position":
            try:
                kwargs["queryset"] = ReactorPosition.objects.filter(reactor_model=Cycle.objects.get(pk=int(request.path.split(sep='/')[-2])).unit.reactor_model)
            except Exception:
                pass
        return super(SourceAssemblyLoadingPatternInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        
class CycleAdmin(admin.ModelAdmin):
    exclude=('remark',)
    extra=0
    inlines=[BurnablePoisonAssemblyLoadingPatternInline,SourceAssemblyLoadingPatternInline]
    list_display=('__str__','get_burnable_poison_assembly_num','get_source_assembly_num')
   
    
    def get_burnable_poison_assembly_num(self,obj):
        num=obj.burnable_posison_assembly_positions.count()
        return num
    get_burnable_poison_assembly_num.short_description='burnable poison assembly count'
    
    def get_source_assembly_num(self,obj):
        num=obj.source_assembly_positions.count()
        return num
    get_source_assembly_num.short_description='source assembly count'
    
admin.site.register(Cycle, CycleAdmin)


#fuel assembly model information
class GridAdmin(admin.ModelAdmin):
    exclude=('remark',)
    
admin.site.register(Grid, GridAdmin)


class GuideTubeInline(admin.TabularInline):
    exclude=('remark',)
    model=GuideTube

class InstrumentTubeInline(admin.TabularInline):
    exclude=('remark',)
    model=InstrumentTube

    
class GridPositionInline(admin.TabularInline):
    exclude=('remark',)
    extra=0
    model=GridPosition

class UpperNozzleInline(admin.TabularInline):
    exclude=('remark',)
    model=UpperNozzle
    
class LowerNozzleInline(admin.TabularInline):
    exclude=('remark',)
    model=LowerNozzle
    
class FuelElementInline(admin.TabularInline):
    exclude=('remark',)
    model=FuelElement
class FuelPelletInline(admin.TabularInline):
    exclude=('remark',)
    model=FuelPellet
     
class FuelAssemblyModelAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_display=('__str__','get_fuel_element_num','get_guide_tube_num','get_instrument_tube_num',)
    inlines=[GridPositionInline,UpperNozzleInline,LowerNozzleInline,GuideTubeInline,InstrumentTubeInline,FuelElementInline,FuelPelletInline]
    
    def get_fuel_element_num(self,obj):
        num=obj.positions.filter(type='fuel').count()
        return num
    get_fuel_element_num.short_description='fuel element count'
    
    def get_guide_tube_num(self,obj):
        num=obj.positions.filter(type='guide').count()
        return num
    get_guide_tube_num.short_description='control rod count'
    
    def get_instrument_tube_num(self,obj):
        num=obj.positions.filter(type='instrument').count()
        return num
    get_instrument_tube_num.short_description='instrument count'
    
admin.site.register(FuelAssemblyModel, FuelAssemblyModelAdmin)

class FuelAssemblyRepositoryAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_filter=['type','plant','cycle_positions__cycle','cycle_positions__reactor_position']
admin.site.register(FuelAssemblyRepository, FuelAssemblyRepositoryAdmin)

#fuel assembly type information
class FuelElementTypePositionInline(admin.TabularInline):
    exclude=('remark',)
    
    model=FuelElementTypePosition

class FuelElementTypePositionAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_filter=['fuel_assembly_type','fuel_element_type']
admin.site.register(FuelElementTypePosition, FuelElementTypePositionAdmin)    

    
    
class FuelAssemblyTypeAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_display=('__str__','assembly_enrichment',)
    list_editable=('assembly_enrichment',)
admin.site.register(FuelAssemblyType, FuelAssemblyTypeAdmin)

class FuelElementPelletLoadingSchemeInline(admin.TabularInline):
    exclude=('remark',)
    extra=0
    model=FuelElementPelletLoadingScheme

class FuelElementTypeAdmin(admin.ModelAdmin):
    exclude=('remark',)
    inlines=[FuelElementPelletLoadingSchemeInline,]
admin.site.register(FuelElementType, FuelElementTypeAdmin)



class FuelPelletTypeAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_display=['model','material']
admin.site.register(FuelPelletType, FuelPelletTypeAdmin)
#the position information of fuel assembly model

    
class FuelAssemblyPositionAdmin(admin.ModelAdmin):
    list_filter=('fuel_assembly_model','row','column')
    list_display=('__str__','type')
    list_editable=('type',)
    ordering=('row','column')
    exclude=('remark',)
    list_per_page=300 
admin.site.register(FuelAssemblyPosition, FuelAssemblyPositionAdmin)



#fuel element information
class UpperCapInline(admin.TabularInline):
    exclude=('remark',)
    model=UpperCap
    
class LowerCapInline(admin.TabularInline):
    exclude=('remark',)
    model=LowerCap
    
class PlenumSpringInline(admin.TabularInline):
    exclude=('remark',)
    model=PlenumSpring
    
class CladdingTubeInline(admin.TabularInline):
    exclude=('remark',)
    model=CladdingTube

    
class FuelElementAdmin(admin.ModelAdmin):
    exclude=('remark',) 
    inlines=[UpperCapInline,LowerCapInline,PlenumSpringInline,CladdingTubeInline]
admin.site.register(FuelElement, FuelElementAdmin)

#fuel pellet type information    
class FuelPelletAdmin(admin.ModelAdmin):
    exclude=('remark',) 
admin.site.register(FuelPellet, FuelPelletAdmin)

class FakeFuelElementTypeAdmin(admin.ModelAdmin):
    exclude=('remark',)
admin.site.register(FakeFuelElementType, FakeFuelElementTypeAdmin)

#########################################################################################
#component assembly rod

class ControlRodTypeAdmin(admin.ModelAdmin):
    exclude=('remark',)
admin.site.register(ControlRodType, ControlRodTypeAdmin)

class SourceRodTypeAdmin(admin.ModelAdmin):
    exclude=('remark',)
admin.site.register(SourceRodType, SourceRodTypeAdmin) 

class NozzlePlugRodAdmin(admin.ModelAdmin):
    exclude=('remark',)
admin.site.register(NozzlePlugRod, NozzlePlugRodAdmin)

class BurnablePoisonMaterialInline(admin.TabularInline):
    model=BurnablePoisonMaterial
    exclude=('remark',) 
    
class BurnablePoisonRodAdmin(admin.ModelAdmin):
    exclude=('remark',)
    inlines=[BurnablePoisonMaterialInline,]
admin.site.register(BurnablePoisonRod, BurnablePoisonRodAdmin) 

############################################################################
#burnable poison assembly

class BurnablePoisonRodMapInline(admin.TabularInline):
    exclude=('remark',)
    model=BurnablePoisonRodMap
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "burnable_poison_position":
            try:
                kwargs["queryset"] = FuelAssemblyPosition.objects.filter(fuel_assembly_model=BurnablePoisonAssembly.objects.get(pk=int(request.path.split(sep='/')[-2])).fuel_assembly_model)
            except Exception:
                pass
            
        return super(BurnablePoisonRodMapInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

    
    
class BurnablePoisonAssemblyAdmin(admin.ModelAdmin):
    exclude=('remark',)
    inlines=[BurnablePoisonRodMapInline]
    list_display=['__str__','get_poison_rod_num']
    
    def get_rod_num(self,obj):
        num=obj.rod_positions.count()
        return num
    get_rod_num.short_description='burnable position rod count'
admin.site.register(BurnablePoisonAssembly, BurnablePoisonAssemblyAdmin)

class BurnablePoisonAssemblyLoadingPatternAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_display=('cycle','reactor_position','burnable_poison_assembly')
    list_filter=('cycle',)
admin.site.register(BurnablePoisonAssemblyLoadingPattern, BurnablePoisonAssemblyLoadingPatternAdmin)
###############################################################################
#control rod assembly   

class ControlRodMapInline(admin.TabularInline):
    exclude=('remark',)
    model=ControlRodMap

class ControlRodAssemblyAdmin(admin.ModelAdmin):
    exclude=('remark',)
    inlines=[ControlRodMapInline,]
admin.site.register(ControlRodAssembly, ControlRodAssemblyAdmin)

class ControlRodAssemblyLoadingPatternAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_display=('reactor_position','control_rod_assembly')
admin.site.register(ControlRodAssemblyLoadingPattern, ControlRodAssemblyLoadingPatternAdmin)


##############################################################################
#source assembly 
class SourceRodMapInline(admin.TabularInline):
    exclude=('remark',)
    extra=0
    model=SourceRodMap
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "source_rod_position":
            try:
                kwargs["queryset"] = FuelAssemblyPosition.objects.filter(fuel_assembly_model=SourceAssembly.objects.get(pk=int(request.path.split(sep='/')[-2])).fuel_assembly_model)
                
            except Exception:
                pass
        return super(SourceRodMapInline, self).formfield_for_foreignkey(db_field, request, **kwargs)    
    
class SourceAssemblyAdmin(admin.ModelAdmin):
    exclude=('remark',)
    inlines=[SourceRodMapInline,]
admin.site.register(SourceAssembly, SourceAssemblyAdmin)

class SourceAssemblyLoadingPatternAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_filter=('cycle',)
admin.site.register(SourceAssemblyLoadingPattern,SourceAssemblyLoadingPatternAdmin)   

################################################################################ 
#nozzle plug assembly
class NozzlePlugRodMapInline(admin.TabularInline):
    exclude=('remark',)
    model=NozzlePlugRodMap

class NozzlePlugAssemblyAdmin(admin.ModelAdmin):
    exclude=('remark',)
    inlines=[NozzlePlugRodMapInline,]
admin.site.register(NozzlePlugAssembly, NozzlePlugAssemblyAdmin)

#####################################################################################

