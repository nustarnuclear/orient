from calculation.models import *
from rest_framework import serializers
from tragopan.models import FuelAssemblyType,FuelAssemblyModel,Grid,GridPosition,UnitParameter,Cycle


class GridSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Grid
        fields = ('sleeve_height','functionality')   
        
class GridPositionSerializer(serializers.ModelSerializer):
    grid=GridSerializer()
    class Meta:
        model = GridPosition
        fields = ( 'height','grid')



class FuelAssemblyModelSerializer(serializers.ModelSerializer):
    grids=GridPositionSerializer(many=True, read_only=True)
    class Meta:
        model=FuelAssemblyModel
        fields=('grids','overall_length')

class FuelAssemblyTypeSerializer(serializers.ModelSerializer):
    model=FuelAssemblyModelSerializer()
    class Meta:
        model=FuelAssemblyType
        fields=('model',)

class IbisSerializer(serializers.ModelSerializer):
    fuel_assembly_type=FuelAssemblyTypeSerializer()
    class Meta:
        model=Ibis
        fields=('ibis_name','fuel_assembly_type','reactor_model','active_length')


class BaseFuelCompositionSerializer(serializers.ModelSerializer):
    ibis=IbisSerializer()
    class Meta:
        model=BaseFuelComposition
        fields=('height','ibis')       
        
class CustomBaseFuelSerializer(serializers.ModelSerializer):
    
    composition=BaseFuelCompositionSerializer(many=True, read_only=True)
    class Meta:
        model=BaseFuel
        fields = ( 'fuel_identity','offset','base_bottom','composition')
        
        
class UnitParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model=UnitParameter
        fields=('plant','unit','reactor_model')
        
        
class CycleSerializer(serializers.ModelSerializer):
   
    
    class Meta:
        model = Cycle
        fields = ( 'unit','fuel_assembly_loading_patterns')
        