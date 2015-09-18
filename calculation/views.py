from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
from calculation.models import *
from calculation.serializers import *
from tragopan.models import ReactorModel
#custom xml render
"""
Provides XML rendering support.
"""

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