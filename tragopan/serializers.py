from rest_framework import serializers
from tragopan.models import *


class ElementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Element
        fields = ('atomic_number', 'symbol', 'nameCH', 'nameEN', 'reference', )
        
        
class ReactorPositionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReactorPosition
        fields = ( 'row','column', )

class FuelAssemblyListingField(serializers.RelatedField):
    def to_representation(self, value):
        
        first_loading_pattern=FuelAssemblyLoadingPattern.objects.filter(fuel_assembly=value).first()
        first_cycle=first_loading_pattern.cycle.cycle
        first_position=first_loading_pattern.reactor_position
        return "{}-{}-{}-{}-{}-{}".format(value.pk, value.type.pk,value.type.assembly_enrichment,first_cycle,first_position.row,first_position.column)

class FuelAssemblyRepositorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FuelAssemblyRepository
        fields = ( 'id','type', )
               
        
class FuelAssemblyLoadingPatternSerializer(serializers.ModelSerializer):
    reactor_position=ReactorPositionSerializer()
    fuel_assembly=FuelAssemblyListingField(read_only=True)
    #previous_reactor_position=serializers.PrimaryKeyRelatedField(query_set=FuelAssemblyLoadingPattern.objects.filter(fuel_assembly=fuel_assembly))
    
    class Meta:
        model = FuelAssemblyLoadingPattern
        fields = ( 'reactor_position','fuel_assembly', 'get_previous','get_grid')
        
class PlantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Plant
        fields = ( 'abbrEN',)       
        
class UnitParameterSerializer(serializers.ModelSerializer):
    plant=PlantSerializer()
    class Meta:
        model = UnitParameter
        fields = ( 'plant','unit')
        
class BurnablePoisonAssemblySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BurnablePoisonAssembly
        fields = ( 'get_poison_rod_num','get_poison_rod_height',)
   
class BurnablePoisonAssemblyLoadingPatternSerializer(serializers.ModelSerializer):
    reactor_position=ReactorPositionSerializer()
    burnable_poison_assembly=BurnablePoisonAssemblySerializer()
    class Meta:
        model = BurnablePoisonAssemblyLoadingPattern
        fields = ( 'reactor_position','burnable_poison_assembly')
        

class CycleSerializer(serializers.ModelSerializer):
    #unit=UnitParameterSerializer()
    fuel_assembly_loading_patterns=FuelAssemblyLoadingPatternSerializer(many=True, read_only=True)
    burnable_posison_assembly_positions=BurnablePoisonAssemblyLoadingPatternSerializer(many=True, read_only=True)
    class Meta:
        model = Cycle
        fields = ( 'fuel_assembly_loading_patterns','burnable_posison_assembly_positions')
        