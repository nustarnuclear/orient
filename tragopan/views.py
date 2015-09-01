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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework import viewsets
       
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
    
@api_view(['GET', 'PUT', 'DELETE'])
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

    elif request.method == 'PUT':
        serializer = CycleSerializer(cycle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cycle.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)        

@api_view(['GET',])
def hello_test(request,format=None):
    BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    os.chdir(BASE_DIR)
    result=os.popen('hello.py').read()
    return Response(result)

