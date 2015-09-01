$(document).ready(function(){
	$('#add_one_element').click(function() {
		var ctr=$('#id_element_input_method option:selected').val();
		if (ctr=='1'){
			var form_idx = $('#id_weight_composition-TOTAL_FORMS').val();
		     $('#weight_composition_formset').append($('#weight_composition_emptyform').html().replace(/__prefix__/g, form_idx));
		     $('#id_weight_composition-TOTAL_FORMS').val(parseInt(form_idx) + 1);
		}
		else{
			var form_idx = $('#id_number_composition-TOTAL_FORMS').val();
		     $('#number_composition_formset').append($('#number_composition_emptyform').html().replace(/__prefix__/g, form_idx));
		     $('#id_number_composition-TOTAL_FORMS').val(parseInt(form_idx) + 1);
		}
	 });

	$('#delete_one_element').click(function() {
		var ctr=$('#id_element_input_method option:selected').val();
		if (ctr=='1'){
			var form_idx = $('#id_weight_composition-TOTAL_FORMS').val();
		    for(i=0;i<5;i++){ $('#weight_composition_formset :last-child').remove();}
		    $('#id_weight_composition-TOTAL_FORMS').val(parseInt(form_idx) - 1);
		}
		else{
			var form_idx = $('#id_number_composition-TOTAL_FORMS').val();
		    for(i=0;i<5;i++){ $('#number_composition_formset :last-child').remove();}
		    $('#id_number_composition-TOTAL_FORMS').val(parseInt(form_idx) - 1);
		}
	});


	$('#add_one_nuclide').click(function() {
		var ctr=$('#id_nuclide_input_method option:selected').val();
		if (ctr=='1'){
			var form_idx = $('#id_weight_nuclide-TOTAL_FORMS').val();
		     $('#weight_nuclide_formset').append($('#weight_nuclide_emptyform').html().replace(/__prefix__/g, form_idx));
		     $('#id_weight_nuclide-TOTAL_FORMS').val(parseInt(form_idx) + 1);
		}
		else{
			var form_idx = $('#id_mole_nuclide-TOTAL_FORMS').val();
		     $('#mole_nuclide_formset').append($('#mole_nuclide_emptyform').html().replace(/__prefix__/g, form_idx));
		     $('#id_mole_nuclide-TOTAL_FORMS').val(parseInt(form_idx) + 1);
		}
	});

	$('#delete_one_nuclide').click(function() {
		var ctr=$('#id_nuclide_input_method option:selected').val();
		if (ctr=='1'){
			var form_idx = $('#id_weight_nuclide-TOTAL_FORMS').val();
		    for(i=0;i<5;i++){ $('#weight_nuclide_formset :last-child').remove();}
		    $('#id_weight_nuclide-TOTAL_FORMS').val(parseInt(form_idx) - 1);
		}
		else{
			var form_idx = $('#id_mole_nuclide-TOTAL_FORMS').val();
		    for(i=0;i<5;i++){ $('#mole_nuclide_formset :last-child').remove();}
		    $('#id_mole_nuclide-TOTAL_FORMS').val(parseInt(form_idx) - 1);
		}
	});
	
	$('#id_element_input_method').change(function(){
		var ctr=$('#id_element_input_method option:selected').val();
		if (ctr=='1'){
			$('#number_composition_formset').css({'display':'none'});
			$('#weight_composition_formset').css({'display':'inline'})
		}
		else{
			$('#number_composition_formset').css({'display':'inline'});
			$('#weight_composition_formset').css({'display':'none'});
		}
	});
	
	$('#id_nuclide_input_method').change(function(){
		var ctr=$('#id_nuclide_input_method option:selected').val();
		if (ctr=='1'){
			$('#mole_nuclide_formset').css({'display':'none'});
			$('#weight_nuclide_formset').css({'display':'inline'});
			$('#add_one_nuclide').css({'display':'inline'});
			$('#delete_one_nuclide').css({'display':'inline'});
		}
		else if(ctr=='2'){
			$('#mole_nuclide_formset').css({'display':'inline'});
			$('#weight_nuclide_formset').css({'display':'none'});
			$('#add_one_nuclide').css({'display':'inline'});
			$('#delete_one_nuclide').css({'display':'inline'});
		}
		else{
			$('#mole_nuclide_formset').css({'display':'none'});
			$('#weight_nuclide_formset').css({'display':'none'});
			$('#add_one_nuclide').css({'display':'none'});
			$('#delete_one_nuclide').css({'display':'none'});
		}
	});
	
	
	$('#weight_composition_formset').on('change','input',function(){
		var share=parseInt($(this).val());
		if(share){alert(share+1);};
	});
	
	
	$('#send').click(function(){
		var composition_idx = $('#id_nuclide-TOTAL_FORMS').val();
		var nuclide_idx = $('#id_composition-TOTAL_FORMS').val();
		var nuclide_sum=0
		
		
	});
})