//common initialize
$(function(){
	
	// all input text was trimmed.
	$(document).on('blur', "input[type='text']", function(){
		$(this).val( $.trim($(this).val()) );
	});
	
});
