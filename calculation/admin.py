from django.contrib import admin
from .models import *
from .functions import *
# Register your models here.

    

    

class PreRobinModelAdmin(admin.ModelAdmin):
    exclude=('remark',)
    
    fieldsets =(
                (None,{
                       'fields':('model_name','user','system_pressure',)
                }),
                
                ('accuracy control',{
                                     'classes': ('grp-collapse grp-closed',),
                                     'fields':('track_density','polar_type','polar_azimuth','iter_inner','iter_outer','eps_keff','eps_flux')
                }),
                ('fundamental mode',{
                                     'classes': ('grp-collapse grp-closed',),
                                     'fields':('leakage_corrector_path','leakage_corrector_method','buckling_or_keff',)
                }),
                ('energy condensation',{
                                        'classes': ('grp-collapse grp-closed',),
                                        'fields':('condensation_path','num_group_2D',)
                                     
                }),
                ('edit control',{
                                 'classes': ('grp-collapse grp-closed',),
                                 'fields':('num_group_edit','micro_xs_output',)
                                     
                }),
    )
    
    class Media:
        js = [
              '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/tinymce_setup.js',
        ]
admin.site.register(PreRobinModel, PreRobinModelAdmin)


class PreRobinBranchAdmin(admin.ModelAdmin):
    fieldsets =(
                (None,{
                       'fields':('identity',)
                }),
                
                ('boron density branch',{
                                     'classes': ('grp-collapse grp-closed',),
                                     'fields':('max_boron_density','min_boron_density','boron_density_interval',)
                }),
                ('fuel temperature branch',{
                                     'classes': ('grp-collapse grp-closed',),
                                     'fields':('max_fuel_temperature','min_fuel_temperature','fuel_temperature_interval',)
                }),
                ('moderator temperature branch',{
                                        'classes': ('grp-collapse grp-closed',),
                                        'fields':('max_moderator_temperature','min_moderator_temperature','moderator_temperature_interval')
                                     
                }),
                ('control rod assembly branch',{
                                 'classes': ('grp-collapse grp-closed',),
                                 'fields':('control_rod_assembly',)
                                     
                }),
                ('shutdown cooling branch',{
                                 'classes': ('grp-collapse grp-closed',),
                                 'fields':('shutdown_cooling_days',)
                                     
                }),
                ('xenon branch',{
                                 'classes': ('grp-collapse grp-closed',),
                                 'fields':('xenon',)
                                     
                }),
    )
admin.site.register(PreRobinBranch, PreRobinBranchAdmin)
    
class PreRobinInputAdmin(admin.ModelAdmin):
    exclude=('remark','pre_robin_file')
    list_display=('segment_identity','plant','pre_robin_file',)
    actions = ['generate_pre_robin_input_file']
    def generate_pre_robin_input_file(self, request, queryset):
        for obj in queryset:
            file=generate_prerobin_input(obj.pk)
            if obj.pre_robin_file:
                obj.pre_robin_file.delete()
            obj.pre_robin_file.save(name=os.path.basename(file),content=file)
        num=len(queryset)
        if num==1:
            self.message_user(request, "%d PreRobin input file successfully generated." % num)
        else:
            self.message_user(request, "%d PreRobin input files successfully generated." % num)
            
    generate_pre_robin_input_file.short_description = "Generate PreRobin Input File"
    
admin.site.register(PreRobinInput, PreRobinInputAdmin)

class IbisAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_display=('__str__','plant','ibis_file','last_modified','burnable_poison_assembly')
    list_editable=('burnable_poison_assembly',)
admin.site.register(Ibis, IbisAdmin)    

class RobinFileAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_display=('__str__','input_file','out1_file','log_file')
admin.site.register(RobinFile, RobinFileAdmin)     

class BaseFuelCompositionInline(admin.TabularInline):
    model=BaseFuelComposition
    exclude=('remark',)


class BaseFuelAdmin(admin.ModelAdmin):
    exclude=('remark',)
    inlines=(BaseFuelCompositionInline,)
    list_display=('__str__','get_ibis_composition','if_insert_burnable_fuel')
    def get_ibis_composition(self,obj):
        ibis_composition=obj.composition.all()
        result=''
        for ibis in ibis_composition:
            result = result+' '+ibis.ibis.ibis_name
        return  result
    get_ibis_composition.short_description='ibis file name'
    
admin.site.register(BaseFuel, BaseFuelAdmin) 
    

class EgretTaskAdmin(admin.ModelAdmin):  
    pass
admin.site.register(EgretTask, EgretTaskAdmin)

class EgretInputXMLAdmin(admin.ModelAdmin):  
    pass
admin.site.register(EgretInputXML, EgretInputXMLAdmin)     

