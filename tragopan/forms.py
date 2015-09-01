from django import forms
from .models import *
from django.core.exceptions import ValidationError

 
class MaterialForm(forms.Form):
    nameCH=forms.CharField(max_length=40,label='Chinese name')
    nameEN=forms.CharField(max_length=40,label='English name')
    density=forms.DecimalField(max_digits=15, decimal_places=5,min_value=0,help_text=r'g/cm3')
    heat_capacity=forms.DecimalField(max_digits=15, decimal_places=5,min_value=0,help_text=r'J/kg*K',required=False)
    thermal_conductivity=forms.DecimalField(max_digits=15, decimal_places=5,min_value=0,help_text=r'W/m*K',required=False)
    expansion_coefficient=forms.DecimalField(max_digits=15, decimal_places=5,min_value=0,help_text=r'm/K',required=False)
    code = forms.CharField(max_length=10,required=False)

class MaterialCompositionByWeightForm(forms.Form):
    element= forms.ModelChoiceField(queryset=Element.objects.all())
    weight_percent=forms.DecimalField(max_digits=9, decimal_places=6,max_value=100,min_value=0)
    
class MaterialCompositionByNumberForm(forms.Form):
    element= forms.ModelChoiceField(queryset=Element.objects.all())
    number=forms.IntegerField(min_value=1,max_value=100)
    
    
class MaterialNuclideByWeightForm(forms.Form):
    nuclide=forms.ModelChoiceField(queryset=Nuclide.objects.all())
    weight_percent=forms.DecimalField(max_digits=9, decimal_places=6,max_value=100,min_value=0)
    
class MaterialNuclideByMoleForm(forms.Form):
    nuclide=forms.ModelChoiceField(queryset=Nuclide.objects.all())
    mole_fraction=forms.DecimalField(max_digits=9, decimal_places=6,max_value=100,min_value=0)

    