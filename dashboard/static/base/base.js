function getCookie(name) {
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				return cookieValue;
			}
		}
	}
}

$.ajaxSetup({
	beforeSend: function(xhr, settings) {
		xhr.setRequestHeader("X-CSRFToken",getCookie('csrftoken'));
	},
});

function doPost(data) {
	$.ajax({
		type: 'POST',
		data: data
	});
}

function postCallback(data,cbFunction) {
	$.ajax({
		type: 'POST',
		data: data,
		success: cbFunction
	});
}