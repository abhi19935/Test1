$('#parseXML').on('click', function() {
		var x12req = $('#X12req').val();

		$.ajax({
			url: '/',
			data: JSON.stringify({'req' : x12req}),
			type: 'POST',
			contentType: 'application/json;charset=UTF-8',		
			success: function(response) {
				var resp = $.parseJSON(response);

				$('#parsedXML').html("<textarea id='xmlparsed'  rows='15' cols='150' readonly>" + resp +  "</textarea>")
			},
			error: function(err) {
				alert("error");
			}
		})
	})