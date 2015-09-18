from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
from calculation.models import *
from calculation.serializers import *
from tragopan.models import ReactorModel,Plant,UnitParameter,Cycle,\
    FuelAssemblyLoadingPattern,ControlRodAssemblyLoadingPattern
#custom xml render
"""
Provides XML rendering support.
"""
from rest_framework import status
from django.utils import six
from django.utils.xmlutils import SimplerXMLGenerator
from django.utils.six.moves import StringIO
from django.utils.encoding import smart_text
from rest_framework.renderers import BaseRenderer
# Create your views here.
class CustomBaseFuelRenderer(BaseRenderer):
    """
    Renderer which serializes to XML.
    """

    media_type = 'application/xml'
    format = 'xml'
    charset = 'utf-8'
    

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML.
        """
        if data is None:
            return ''
        print(data)

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        reactor_model_id=data[0]['composition'][0]['ibis']['reactor_model']
        xml.startElement("base_component ", {'basecore_ID':ReactorModel.objects.get(pk=reactor_model_id).name})

        self._to_xml(xml, data)

        xml.endElement("base_component ")
        xml.endDocument()
        return stream.getvalue()

    def _to_xml(self, xml, data):
        
        #base fuel
        for item in data:
            base_fuel_attr={}
            base_fuel_attr['fuel_identity']=item['fuel_identity']
            base_fuel_attr['offset']='1' if item['offset'] else '0'
            base_fuel_attr['base_bottom']=item['base_bottom']
            base_fuel_attr['active_length']=item['composition'][0]['ibis']['active_length']
            xml.startElement('base_fuel',base_fuel_attr)
            
            
            composition_lst=item['composition']
            ratio_lst=[]
            color_lst=[]
            for i in composition_lst:
                ratio_lst.append(i['height'])
                color_lst.append(i['ibis']['ibis_name'])
                
            xml.startElement('axial_ratio',{})
            xml.characters(smart_text(' '.join(ratio_lst)))
            xml.endElement('axial_ratio' )
            
            xml.startElement('axial_color',{})
            xml.characters(smart_text(' '.join(color_lst)))
            xml.endElement('axial_color')
            
            #grid only choose the first one
            fuel_assembly_type=composition_lst[0]['ibis']['fuel_assembly_type']
            fuel_assembly_model=fuel_assembly_type['model']
            
            
            for grid in fuel_assembly_model['grids']:
                grid_attr={}
                grid_attr['hight']=grid['height']
                grid_attr['width']=grid['grid']['sleeve_height']
                type=1 if grid['grid']['functionality']=='fix' else 0
                xml.startElement('spacer_grid',grid_attr)
                xml.characters(smart_text(type))
                xml.endElement('spacer_grid')
                                
            xml.endElement('base_fuel' )
        #base control rod
        xml.startElement('base_control_rod',{'cr_id':"CR1",'spider':"0"})
        
        xml.startElement('axial_length',{})
        xml.characters(smart_text(400.0))
        xml.endElement('axial_length' )
        
        xml.startElement('axial_type',{})
        xml.characters(smart_text(1))
        xml.endElement('axial_type' )
        
        xml.endElement('base_control_rod' )
            
        

        

@api_view(('GET',))
@renderer_classes((CustomBaseFuelRenderer,))
def BaseFuel_list(request,format=None):
    """ 
    List all fuel assembly type
    """
    if request.method == 'GET':
        base_fuels=BaseFuel.objects.all()
        serializer = CustomBaseFuelSerializer(base_fuels,many=True)
        print(serializer.data)
        return Response(serializer.data)
    




class CustomBaseCoreRenderer(BaseRenderer):
    """
    Renderer which serializes to XML.
    """

    media_type = 'application/xml'
    format = 'xml'
    charset = 'utf-8'
    item_tag_name = 'list-item'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML.
        """
        if data is None:
            return ''
        print(data)

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        reactor_model=ReactorModel.objects.get(pk=data['unit']['reactor_model'])
        fuel_assembly_model=FuelAssemblyLoadingPattern.objects.get(pk=data['fuel_assembly_loading_patterns'][0]).fuel_assembly.type.model
        xml.startElement("basecore ", {'ID':reactor_model.name,'core_type':reactor_model.reactor_type})
        reactor_positions=reactor_model.positions.all()
        num_side_asms=0
        for reactor_position in reactor_positions:
            if reactor_position.row>num_side_asms:
                num_side_asms=reactor_position.row
        #core_geo
        xml.startElement('core_geo',{'num_side_asms':str(num_side_asms)})
        
        
        xml.startElement('fuel_pitch',{})
        xml.characters(smart_text(fuel_assembly_model.assembly_pitch))
        xml.endElement('fuel_pitch')
        
        xml.startElement('std_fuel_len',{})
        xml.characters(smart_text(fuel_assembly_model.fuel_elements.active_length))
        xml.endElement('std_fuel_len')   
        
        xml.startElement('fuel_map',{})
        fuel_map_lst=[]
        for i in range(1,num_side_asms+1):
            for j in range(1,num_side_asms+1):
                fuel_position=reactor_model.positions.filter(row=i,column=j)
                if fuel_position:
                    fuel_map_lst.append('1')
                else:
                    fuel_map_lst.append('0')
        
        xml.characters(smart_text(' '.join(fuel_map_lst)))
        xml.endElement('fuel_map')
        
        xml.endElement('core_geo')   
        
        #control rod map
        xml.startElement('rcca',{})
        control_rod_assembly_lst=[]
        bank_id_lst=[]
        
        for position in reactor_positions:
            try:
                cralp=ControlRodAssemblyLoadingPattern.objects.get(reactor_position=position)
                control_rod_assembly_lst.append(cralp.control_rod_assembly.cluster_name)
                if cralp.control_rod_assembly.cluster_name not in bank_id_lst:
                    bank_id_lst.append(cralp.control_rod_assembly.cluster_name)
            except Exception:
                control_rod_assembly_lst.append('0')
         
        index=1       
        for name in bank_id_lst:
            xml.startElement('bank_id',{'basez':"9.5875",'index':str(index)})
            index+=1
            xml.characters(smart_text(name))
            xml.endElement('bank_id') 
            
        xml.startElement('map',{})    
        xml.characters(smart_text(' '.join(control_rod_assembly_lst)))
        xml.endElement('map') 
        
        xml.startElement('step_size',{})    
        xml.characters(smart_text(1.5832))
        xml.endElement('step_size') 

        xml.endElement('rcca') 
        
        #reflector
        xml.startElement('reflector',{})    
        
        xml.startElement('bot_br',{})
        xml.characters(smart_text('BR_BOT'))    
        xml.endElement('bot_br') 
        
        xml.startElement('top_br',{})
        xml.characters(smart_text('''
        BR_TOP
        BR_TOP BR_TOP
        BR_TOP BR_TOP BR_TOP
        BR_TOP BR_TOP BR_TOP BR_TOP
        BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP
        BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP
        BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP
        BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP
        BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP
        BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP
        BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP BR_TOP
        BR_TOP BR_TOP BR_TOP
        BR_TOP BR_TOP BR_TOP'''))    
        xml.endElement('top_br')
        
        xml.startElement('radial_br',{'index':'1'})
        xml.characters(smart_text('BR3  BR3  BR3  BR9  BR6  BR5  BR7  BR3  BR3  BR9  BR6  BR5  BR7  BR9 '))    
        xml.endElement('radial_br') 
        
        xml.startElement('radial_br',{'index':'2'})
        xml.characters(smart_text('BR4  BR4  BR4 BR10 BR12 BR11  BR8  BR4  BR4 BR10 BR12 BR11  BR8 BR10 BR12'))    
        xml.endElement('radial_br') 
        
        xml.endElement('reflector') 
        

        

        xml.endElement("basecore ")
        xml.endDocument()
        return stream.getvalue()

    

@api_view(('GET','POST'))
@renderer_classes((CustomBaseCoreRenderer,))    
def BaseCore_detail(request, plantname,unit_num,cycle_num,format=None):
    
    try:
        plant=Plant.objects.get(abbrEN=plantname)
        unit=UnitParameter.objects.get(plant=plant,unit=unit_num)
        cycle = Cycle.objects.get(unit=unit,cycle=cycle_num)
    except plant.DoesNotExist or unit.DoesNotExist or cycle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CycleSerializer(cycle)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data=request.data
        return Response(data)
        
    