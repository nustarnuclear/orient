import os
from .models import *
from django.core.files import File

def generate_prerobin_input(input_id):
    pri=PreRobinInput.objects.get(pk=input_id)
    #get segment id
    sid=pri.segment_identity
    #get use_pre_segment
    ups=pri.use_pre_segment
    #get prerobin model
    prm=pri.pre_robin_model
    #get the fuel assembly type
    fat=pri.fuel_assembly_type
    #get burnable_poison_assembly
    bpa=pri.burnable_poison_assembly
    #get grid
    grid=pri.grid
    #get reflector
    cb=pri.core_baffle
    #get branches
    brc=pri.branch_composition.all()
    #get power density
    pd=pri.power_density

    #check if having use_pre_segment
    if not ups:
        
        #built the fuel assembly model
        #get fuel assembly mode
        fam=fat.model

        #when satisfy 1/8 sysmetry
        
        #get this file path
        path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #generate a file
        f=open(os.path.join(path, sid.strip()+'.inp'),mode='w+')
        sep='\n'
        #################################################################material data bank starts
        #material databank
        f.write('material_databank:%s'%sep)
        enrichment=fat.assembly_enrichment
        
        #fuel element type
        fet=fat.fuel_element_Type_position.first()
        #fuel element model
        fem=fet.model
        #fuel pellet type
        pellet=fet.pellet.first()
        #fuel pellet model
        fpm=pellet.model
        #UO2 Nominal density
        nd=fpm.nominal_density
        #fuel material
        f.write('   base_mat:%s'%sep)
        f.write('      ID = {}{}'.format('FUEL_1',sep))
        f.write('      density = {}{}'.format(nd,sep))
        f.write('      composition_ID = UO2_{}{}'.format(enrichment,sep))
        f.write('   /base_mat%s'%sep)
        #
        
        
        f.write('/material_databank%s'%sep)
        #################################################################material data bank ends
        #################################################################pin data bank starts
        #pin databank
        f.write('pin_databank:%s'%sep)
        
        #fuel material map
        fuel_radii=fpm.outer_diameter/2
        #guide tube
        guide_inner_radii=fam.guidetube.upper_inner_diameter/2
        guide_outer_radii=fam.guidetube.upper_outer_diameter/2
        guide_material=fam.guidetube.material
        #filling gas material
        fgm=fem.filling_gas_material
        material_lst=['FUEL',fgm.prerobin_identifier,guide_material.prerobin_identifier,]
        radii_lst=[str(fuel_radii),str(guide_inner_radii),str(guide_outer_radii)]
        #fuel pin
        f.write('   base_pin:%s'%sep)
        f.write('      ID = {}{}'.format('FUEL',sep))
        f.write('      radii = {}{}'.format(','.join(radii_lst),sep))
        f.write('      mat = {}{}'.format(','.join(material_lst),sep))
        f.write('   /base_pin%s'%sep)
        #guide tube pin
        f.write('   base_pin:%s'%sep)
        f.write('      ID = {}{}'.format('GT',sep))
        f.write('      radii = {}{}'.format(','.join([str(guide_inner_radii),str(guide_outer_radii),]),sep))
        f.write('      mat = {}{}'.format(','.join(['MOD',guide_material.prerobin_identifier]),sep))
        f.write('   /base_pin%s'%sep)
        #instrument pin
        f.write('   base_pin:%s'%sep)
        f.write('      ID = {}{}'.format('IT',sep))
        f.write('      radii = {}{}'.format(','.join([str(guide_inner_radii),str(guide_outer_radii),]),sep))
        f.write('      mat = {}{}'.format(','.join(['MOD',guide_material.prerobin_identifier]),sep))
        f.write('   /base_pin%s'%sep)
        #control rod pin
        for br in brc:
            cra=br.control_rod_assembly
            if cra: 
                control_rod_type=cra.control_rods.first().control_rod_type
                absorb_diameter=control_rod_type.absorb_diameter
                absorb_material=control_rod_type.absorb_material
                cladding_material=control_rod_type.cladding_material
                cladding_inner_diameter=control_rod_type.cladding_inner_diameter
                cladding_outer_diameter=control_rod_type.cladding_outer_diameter
                cra_radii_lst=[str(absorb_diameter/2),str(cladding_inner_diameter/2),str(cladding_outer_diameter/2),str(guide_inner_radii),str(guide_outer_radii)]
                cra_material_lst=[absorb_material.prerobin_identifier,fgm.prerobin_identifier,cladding_material.prerobin_identifier,'MOD',guide_material.prerobin_identifier]
                
                f.write('   base_pin:%s'%sep)
                f.write('      ID = {}{}'.format('CRD',sep))
                f.write('      radii = {}{}'.format(','.join(cra_radii_lst),sep))
                f.write('      mat = {}{}'.format(','.join(cra_material_lst),sep))
                f.write('   /base_pin%s'%sep)
        f.write('/pin_databank%s'%sep)     
        
        #################################################################pin data bank ends
        #################################################################branch calculation starts
        #branch databank
        f.write('branch_calc_databank:%s'%sep)
        
        #base branch
        for br in brc:
            br_id=br.identity
            mbd=br.max_boron_density
            mft=br.max_fuel_temperature
            mmt=br.max_moderator_temperature
            cra=br.control_rod_assembly
            scd=br.shutdown_cooling_days
            f.write('   base_branch:%s'%sep)
            f.write('      ID = {}{}'.format(br_id,sep))
            #boron density section
            if mbd:
                boron_point=br.min_boron_density
                if mbd==boron_point:
                    f.write('      BOR = {}{}'.format(str(mbd),sep))
                else:    
                    boron_sep=br.boron_density_interval
                    boron_lst=[]
                    while boron_point<mbd:
                        boron_lst.append(str(boron_point))
                        boron_point += boron_sep
                    boron_lst.append(str(mbd)) 
                    boron_str=','.join(boron_lst)
                    f.write('      BOR = {}{}'.format(boron_str,sep))
                      
            #fuel temperature section
            if mft:
                fuel_point=br.min_fuel_temperature
                if mft==fuel_point:
                    f.write('      TFU = {}{}'.format(str(mft),sep))
                else:    
                    fuel_sep=br.fuel_temperature_interval
                    fuel_lst=[]
                    while fuel_point<mft:
                        fuel_lst.append(str(fuel_point))
                        fuel_point += fuel_sep
                        
                    fuel_lst.append(str(mft)) 
                    fuel_str=','.join(fuel_lst)
                    f.write('      TFU = {}{}'.format(fuel_str,sep)) 
                    
            #moderator temperature section
            if mmt:
                moderator_point=br.min_moderator_temperature
                if mmt==moderator_point:
                    f.write('      TMO = {}{}'.format(str(mmt),sep))
                else:    
                    moderator_sep=br.moderator_temperature_interval
                    moderator_lst=[]
                    while moderator_point<mmt:
                        moderator_lst.append(str(moderator_point))
                        moderator_point += moderator_sep
                        
                    moderator_lst.append(str(mmt)) 
                    moderator_str=','.join(moderator_lst)
                    f.write('      TMO = {}{}'.format(moderator_str,sep))
                    
            #control rod assembly section
            if cra:
                #control rod position 
                control_rod_map=cra.control_rod_map.all()
                #pin map
                pos=fam.positions
                num_pin=pos.filter(row=1).count()
                it=pos.filter(type='instrument').get()
                it_row=it.row
                it_column=it.column
                f.write('      CRD =  NONE%s'%sep)
                for i in range(num_pin-it_column):
                    tmp=pos.filter(row=it_row+i+1,column__lte=it_column+i+1,column__gte=it_column)
                    tmp_lst=[]
                    for tm in tmp:
                        if tm in control_rod_map:
                            tmp_lst.append('CRD ')
                        else:
                            tmp_lst.append('NONE')
                    tmp_str=' '.join(tmp_lst)
                    f.write('             {}{}'.format(tmp_str,sep))
            
            #shutdown_cooling_days section
            if scd:
                scd_int=[1,2,3,5]
                scd_index=0
                scd_lst=[]
                days=scd_int[scd_index]*10
                while days<scd:
                    scd_lst.append(str(days))
                    scd_index = scd_index + 1 
                    mod=scd_index%4
                    days=int(scd_int[mod]*(10**((scd_index-mod)/4+1)))
                
                scd_lst.append(str(scd))
                scd_str=','.join(scd_lst)
                f.write('      SDC = {}{}'.format(scd_str,sep))
                
            #xenon section
            if br.xenon:
                f.write('      XEN = {}{}'.format(1,sep))
                      
            f.write('   /base_branch%s'%sep) 
            
        f.write('/branch_calc_databank%s'%sep)
        
        #################################################################branch calculation ends
        #################################################################calculation segment starts
        #calculation_segment
        f.write('calculation_segment:%s'%sep)
        #f.write('%s'%sep)
        
        #segment_ID
        f.write('   segment_ID = {}{}'.format(sid,sep))
        #get all the branches ids
        ids=[i.identity for i in brc ]
        strid=','.join(ids)
        #branch_calc_ID
        f.write('   branch_calc_ID = {}{}'.format(strid,sep))
        
        #assembly_model
        f.write('   assembly_model:%s'%sep)
        #model_ID
        f.write('   model_ID = {}{}'.format(fam.name,sep))
        #if have grid
        if grid:
            f.write('      moderator_mat = {}{}'.format(grid.sleeve_material.prerobin_identifier,sep))
        
        #spacer_grid_mat
        spacer=fam.grids.first().grid
        f.write('      spacer_grid_mat = {}{}'.format(spacer.sleeve_material.prerobin_identifier,sep))

        #symmetry
        f.write('      symmetry = 8%s'%sep)
        #num_pin_side
        pos=fam.positions
        num_pin=pos.filter(row=1).count()
        f.write('      num_pin_side = {}{}'.format(num_pin,sep))
        #pitch_assembly
        f.write('      pitch_assembly = {}{}'.format(fam.assembly_pitch,sep))
        #pitch_cell
        f.write('      pitch_cell = {}{}'.format(fam.pin_pitch,sep))
        #pin map
        it=pos.filter(type='instrument').get()
        it_row=it.row
        it_column=it.column
        f.write('      pin_map = IT%s'%sep)
        for i in range(num_pin-it_column):
            tmp=pos.filter(row=it_row+i+1,column__lte=it_column+i+1,column__gte=it_column)
            tmp_lst=[]
            for tm in tmp:
                if tm.type=='instrument':
                    tmp_lst.append('IT  ')
                elif tm.type=='fuel':
                    tmp_lst.append('FUEL')
                else:
                    tmp_lst.append('GT  ')
                    
            tmp_str='   '.join(tmp_lst)
            #17 blank space
            f.write('                {}{}'.format(tmp_str,sep))

        f.write('%s'%sep)
        #assembly model complete
        f.write('   /assembly_model%s'%sep)
        f.write('%s'%sep)

        #depletion        
        if pd:
            f.write('   depletion_state:%s'%sep)
            f.write('      burnup_point = {}{}'.format(-pri.assembly_maxium_burnup,sep))
            f.write('      power_density = {}{}'.format(pd,sep))
            f.write('      BOR = {}{}'.format(pri.boron_density,sep))
            f.write('      TMO = {}{}'.format(pri.moderator_temperature,sep))
            f.write('      TFU = {}{}'.format(pri.fuel_temperature,sep))
            f.write('   /depletion_state%s'%sep)
            #f.write('%s'%sep)

        f.write('/calculation_segment%s'%sep)
        ######################################################calculation segment ends
    
    return File(f)
