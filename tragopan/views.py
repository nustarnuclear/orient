from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.db.models import Sum,F
from .forms import *
from tragopan.models import Element,Cycle
import os
#django rest framework
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from tragopan.serializers import ElementSerializer,FuelAssemblyLoadingPatternSerializer,CycleSerializer
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework import viewsets


#custom xml render
"""
Provides XML rendering support.
"""

from django.utils import six
from django.utils.xmlutils import SimplerXMLGenerator
from django.utils.six.moves import StringIO
from django.utils.encoding import smart_text
from rest_framework.renderers import BaseRenderer

class CustomXMLRenderer(BaseRenderer):
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

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        xml.startElement("orient", {'test':'test'})

        self._to_xml(xml, data)

        xml.endElement("orient")
        xml.endDocument()
        return stream.getvalue()

    def _to_xml(self, xml, data):
        if isinstance(data, (list, tuple)):
            for item in data:
                xml.startElement(self.item_tag_name, {})
                self._to_xml(xml, item)
                xml.endElement(self.item_tag_name)

        elif isinstance(data, dict):
            for key, value in six.iteritems(data):
                try:
            
                    tmp_lst=value.split(sep='~')
                    attr_dic={}
                    for i in range(1,len(tmp_lst)):
                        if i %2 != 0:
                            attr_dic[tmp_lst[i]]=tmp_lst[i+1]
                            
                    xml.startElement(key, attr_dic)
                    self._to_xml(xml, tmp_lst[0])
                    xml.endElement(key)
                except AttributeError:
                    xml.startElement(key, {})
                    self._to_xml(xml, value)
                    xml.endElement(key)
                

        elif data is None:
            # Don't output any value
            pass

        else:
            xml.characters(smart_text(data))




       
class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)
    
class CylcleViewSet(viewsets.ModelViewSet):
    
    serializer_class = CycleSerializer
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)
    
    def get_queryset(self):
       
        plantname = self.kwargs['plantname']
        unit_num = self.kwargs['unit_num']
        cycle_num = self.kwargs['cycle_num']
        
        try:
            plant=Plant.objects.get(abbrEN=plantname)
            unit=UnitParameter.objects.get(plant=plant,unit=unit_num)
            cycle = Cycle.objects.get(unit=unit,cycle=cycle_num)
            return cycle
        except Cycle.DoesNotExist or Plant.DoesNotExist or UnitParameter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['GET', 'POST'])
def fuel_assembly_loading_pattern_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        fuel_assembly_loading_patterns = FuelAssemblyLoadingPattern.objects.all()
        serializer = FuelAssemblyLoadingPatternSerializer(fuel_assembly_loading_patterns, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FuelAssemblyLoadingPatternSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def fuel_assembly_loading_pattern_detail(request, pk,format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        fuel_assembly_loading_pattern = FuelAssemblyLoadingPattern.objects.get(pk=pk)
    except FuelAssemblyLoadingPattern.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FuelAssemblyLoadingPatternSerializer(fuel_assembly_loading_pattern)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FuelAssemblyLoadingPatternSerializer(fuel_assembly_loading_pattern, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fuel_assembly_loading_pattern.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def cycle_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        cycles = Cycle.objects.all()
        serializer = CycleSerializer(cycles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CycleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
 
    
@api_view(('GET',))
@renderer_classes((CustomXMLRenderer,))
def cycle_detail(request, plantname,unit_num,cycle_num,format=None):
    """
    Retrieve, update or delete a code snippet.
    """
   
   
    try:
        plant=Plant.objects.get(abbrEN=plantname)
        unit=UnitParameter.objects.get(plant=plant,unit=unit_num)
        cycle = Cycle.objects.get(unit=unit,cycle=cycle_num)
    except Cycle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CycleSerializer(cycle)
        return Response(serializer.data)



    
      

@api_view(['GET',])
def hello_test(request,format=None):
    BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    os.chdir(BASE_DIR)
    result=os.popen('hello.py').read()
    return Response(result)





