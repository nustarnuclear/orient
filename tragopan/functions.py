#function that handle the transformation between weight and mole
from decimal import Decimal
from .models import *
import os
'''
def weight_to_mole(*args, inverse=False):
    'transform the weight percent of nuclide to mole fraction;
    input  a couple of lists with format[atom_mass,weight_percent];
    the result is list of mole fraction with the corresponding order;
    when set inverse=True,you can transform mole to weight'
    import numpy as np
    length=len(args)
    matrix=np.array(args)
    atom_mass=matrix[range(length),0]
    mole_or_weight=matrix[range(length),1]

    if abs(mole_or_weight.sum()-1) >1e-10:
        print(mole_or_weight.sum())
        raise Exception("the weight percent or mole fraction sum don't equal to 1")
    if not inverse:
        B=np.zeros((length,1))
        A=np.zeros((length,length))
        diagonal_num=[]
        row_num=[]
        for arg in args:
            mass=arg[0]
            percent=arg[1]
            row_num.append(mass)
            diagonal_num.append(mass-mass/percent)
       
        for i in range(length):
            A[i]=row_num
            A[i,i]=diagonal_num[i]

        A[length-1]=1
        B[length-1]=1
        result=np.linalg.solve(A,B)
        lst=[]
        element_mass=0
        for i in range(length):
            lst.append(Decimal(result[i,0]))
            element_mass +=Decimal(result[i,0])*Decimal(atom_mass[i])
        
        
    else:
        B=atom_mass*mole_or_weight

        element_mass=atom_mass.T.dot(mole_or_weight)

        result=B/element_mass
        lst=[Decimal(i) for i in list(result)]

    return [Decimal(element_mass),lst]
'''

def generate_assembly_position(number=17):
    positions=[]
    for i in range(1,number*number+1):
        md=i%number
        if md ==0:
            column=number
        else:
            column=md
        row=(i-column)/number+1
        positions.append([round(row),column])
    return positions 
def get_U_enrichment(u):
    u234=round(1.036*u-0.449,5)
    u236=round(0.0201*u+0.0459,5)
    u238=100-round(u234+u236+u,5)
    return [u,u234,u236,u238]

def add_fuel_assembly_type(id1,id2):
    '''id1 represent the fuel assembly type,
    id2 represent the fuel element type'''
    
    #get the fuel assembly type
    ft=FuelAssemblyType.objects.get(pk=id1)
    #get the fuel assembly model
    fm=ft.model
    #get the fuel position
    fp=fm.positions.filter(type='fuel')
    #get the fuel element type
    fe=FuelElementType.objects.get(pk=id2)
    for position in fp:
        ftp=FuelElementTypePosition(fuel_assembly_type=ft,fuel_assembly_position=position,fuel_element_type=fe)
        ftp.save()
    
def add_fuel_assembly_repository(id1,id2,num):
    '''id1 represent the fuel assembly type;
    id2 represent the plant;num represent the number of fuel assembly you want to add '''
    #get the fuel assembly type
    ft=FuelAssemblyType.objects.get(pk=id1)
    #get the plant
    pl=Plant.objects.get(pk=id2)
    
    for i in range(num):
        far=FuelAssemblyRepository(type=ft,plant=pl)
        far.save()
        
def add_cycle_position(id):
    '''id represent the cycle;'''
    #get the cycle
    cy=Cycle.objects.get(pk=id)
    #get the reactor model
    rm=cy.unit.reactor_model
    #get the reactor model positions 
    positions=rm.positions.all()
    for position in positions:
        falp=FuelAssemblyLoadingPattern(cycle=cy,reactor_position=position)
        falp.save()
        
def fuel_assembly_loading_pattern(id,filename):
    '''id represent the cycle;'''
    #get the fuel assembly loading pattern corresponding to the cycle
    falps=FuelAssemblyLoadingPattern.objects.filter(cycle_id=id)
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR=os.path.join(BASE_DIR, 'data')
    FILE_PATH=os.path.join(DATA_DIR,filename+'.txt')
    f=open(FILE_PATH,'r')
    num_lst=f.read().split()
    #the number in num represent the fuel assembly id
    num=[int(i) for i in num_lst ]
    f.close()
    for i in range(len(num)):
        #get the fuel assembly
        fa=FuelAssemblyRepository.objects.get(pk=num[i])
        falp=falps[i]
        falp.fuel_assembly=fa
        falp.save()
        
        
def generate_relative_position(plant_id,unit_num,cycle_id,*ids):
    '''ids represent all the fresh assembly start id'''
    #get the plant
    p=Plant.objects.get(pk=plant_id)
    #get the unit
    u=p.unitparameter_set.filter(unit=unit_num).get()
    #get the reactor model
    rm=u.reactor_model
    #get the fuel assembly loading pattern corresponding to the cycle
    falps=FuelAssemblyLoadingPattern.objects.filter(cycle_id=cycle_id)
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR=os.path.join(os.path.join(BASE_DIR, 'data'),'position')
    FILE_PATH=os.path.join(DATA_DIR,str(plant_id)+'-'+str(unit_num)+'-C'+str(cycle_id)+'.txt')
    f=open(FILE_PATH,'r')
    x=f.read().split()
    y=[]
    index=[0 for i in range(len(ids))]
    for i in range(len(x)):
        lst=x[i].split('_')
        if len(lst)!=2:
            lst.append(cycle_id-1)
            
        if lst[0].upper() !='NEW':
            row=ord(lst[0][0])
            if row<73:
                row -=64
            else:
                row -=65
                
            column=int(lst[0][1:3])
            pre_cycle=Cycle.objects.get(pk=int(lst[1]))
            position_num=rm.positions.filter(row=row,column=column).get()
            pattern=FuelAssemblyLoadingPattern.objects.filter(cycle=pre_cycle,reactor_position=position_num).get()
            assembly_num=pattern.fuel_assembly.pk
            result=assembly_num
        else:
            start_id=ids[int(lst[1])-1]
            interval=index[int(lst[1])-1]
            index[int(lst[1])-1] +=1
            result=start_id+interval
                 
        y.append(result)
    
    for i in range(len(y)):
        #get the fuel assembly
        fa=FuelAssemblyRepository.objects.get(pk=y[i])
        falp=falps[i]
        falp.fuel_assembly=fa
        falp.save()
        
    f.close()
    return y 

def count_fresh_num(plant_id,unit_num,cycle_id,num):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR=os.path.join(os.path.join(BASE_DIR, 'data'),'position')
    FILE_PATH=os.path.join(DATA_DIR,str(plant_id)+'-'+str(unit_num)+'-C'+str(cycle_id)+'.txt')
    f=open(FILE_PATH,'r')
    x=f.read().split()
    index=[0 for i in range(num)]
    
    for i in range(len(x)):
        lst=x[i].split('_')
        if lst[0].upper() =='NEW':
            index[int(lst[1])-1] +=1
    print(index)
    f.close()
    return index

def map_to_position(plant,unit):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR=os.path.join(os.path.join(os.path.join(BASE_DIR, 'data'),plant),unit)
    FILE_PATH=os.path.join(DATA_DIR,'c1.txt')
    f=open(FILE_PATH)
    t=f.read()
    s=t.split(sep='\n')
    
    positions=[]
    for i in range(len(s)):
        p=s[i].split(sep='\t')
        row=i+1
        for j in range(len(p)):
            try:
                int(p[j])
                column=j+1
                positions.append([row,column])
            except ValueError:
                pass
    f.close()   
    return positions

def add_contrl_rod_map(id):
    '''id represent the fuel assembly model,
    this function only suit for the same rod type'''
    #get fuel assembly mode
    fa=FuelAssemblyModel.objects.get(pk=id)
    #get control rod assembly
    crs=ControlRodAssembly.objects.filter(fuel_assembly_model=fa)
    #get the rod type
    ct=ControlRodType.objects.filter(fuel_assembly_model=fa).get()
    #get the guide tube position
    positions=FuelAssemblyPosition.objects.filter(fuel_assembly_model=fa,type='guide')
    for cr in crs:
        for position in positions:
            crm=ControlRodMap(control_rod_assembly=cr,guide_tube_position=position,control_rod_type=ct)
            crm.save()
        
        
def add_wmis_nuclide_data(filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR=os.path.join(BASE_DIR, 'data')
    FILE_PATH=os.path.join(DATA_DIR,filename)
    print(FILE_PATH)
    f=open(FILE_PATH)
    t=f.read()
    print(t)
    s=t.split(sep='\n')
    print(s)
    
    for i in s:
        tmp=i.split()
        id_wims=int(tmp[1])
        wn=WimsNuclideData.objects.get(id_wims=id_wims)
        wn.id_self_defined=int(tmp[0])
        wn.save()
    
    
def add_wmis_element_data(filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR=os.path.join(BASE_DIR, 'data')
    FILE_PATH=os.path.join(DATA_DIR,filename)
    f=open(FILE_PATH)
    t=f.read()
    
    s=t.split()
    for i in range(len(s)):
        try:
            Decimal(s[i])
        except:
            name=s[i]
            try:
                obj=WmisElementData.objects.get(element_name=name)
            except:
                obj=WmisElementData(element_name=name)
                obj.save()
                
            num=int(s[i+1])
            for j in range(i+1,i+1+2*num):
                if j%2==0:
                    wn=WimsNuclideData.objects.get(id_self_defined=int(s[j]))
                    wp=Decimal(s[j+1])*100
                    we=WmisElementComposition(wmis_element=obj,wmis_nuclide=wn,weight_percent=wp)
                    we.save()
                    print(we)
        
    print(s)