var position;

$("#timeFrom").timepicker({ 
	'scrollDefaultNow': true 
});

function getPosition(){
	console.log("Getting Location");
	if(navigator.geolocation)
		navigator.geolocation.getCurrentPosition(showPosition(position));
	else
		console.log("NOT SUPPORTED");
		//x.innerHTML = "Geolocation is not supported by this browser.";
}

function showPosition(position){
	console.log("This shit works");
	console.log(position);
	$.get('functions/cityLookup.php',{'lat': position.coords.latitude,'lon':position.coords.longitude},function(userdata){
		user_array = jQuery.parseJSON(userdata);
		for(i in user_array){
			dataInLoop = user_array[i];
			for(j in dataInLoop){
				cityName = dataInLoop[j];
				for(k in cityName.address_components){
					city = cityName.address_components[k];
					for(l in city.types){
						if(city.types[l] == 'locality'){
							$("#loc").val(city.long_name);
							return;
						}
					}
				}
			}
		}
	});
	
	$.get('getVenue',{'lat': position.coords.latitude,'lon':position.coords.longitude},function(userdata){
		
	});
	
	console.log("FUCK");
}
