var position;

$("#timeFrom").timepicker({ 
	'scrollDefaultNow': true 
});

function getPosition(){
	if(navigator.geolocation)
		navigator.geolocation.getCurrentPosition(showPosition);
	else
		alert("Geolocation is not supported by this browser.");
}

var map;
var foursquarePlaces;

function showPosition(position)
{
			console.log(position.coords.latitude + ',' + position.coords.longitude);
	
	if(map==null)
	{
		map = L.mapbox.map('map', 'siddharthmodala.hpcjnnaf', {
        attributionControl: true
		})
		.setView([position.coords.latitude, position.coords.longitude], 10);
		
		map.attributionControl
    .addAttribution('<a href="https://foursquare.com/">Places data from Foursquare</a>');

	}
	
	// Credit Foursquare for their wonderful data
	
	
	var CLIENT_ID = 'ETWY3CHBMEFXU2DZZZ1DKTO2YPMNKJWNZTVSKBABBXTQEDW2';
	var CLIENT_SECRET = 'X0H2FBGJ53ANMC23YHWQKI0LV5I52F12MWZMF5002EOJ0NSR';


	var API_ENDPOINT = 'https://api.foursquare.com/v2/venues/explore' +
	'?client_id=CLIENT_ID' +
	'&client_secret=CLIENT_SECRET' +
	'&v=20130815' +
	'&ll=LATLON' +
	'&section=drinks'+
	'&limit=10'+
	'&callback=?';
  

	// Keep our place markers organized in a nice group.
	
	if(foursquarePlaces == null)
	{foursquarePlaces = L.layerGroup().addTo(map);  }
	else
	{
	foursquarePlaces.clearLayers();	
	}

	
	/*console.log(API_ENDPOINT
    .replace('CLIENT_ID', CLIENT_ID)
    .replace('CLIENT_SECRET', CLIENT_SECRET)
    .replace('LATLON', position.coords.latitude +
        ',' + position.coords.longitude));*/
	// Use jQuery to make an AJAX request to Foursquare to load markers
	// data.
	$.getJSON(API_ENDPOINT
    .replace('CLIENT_ID', CLIENT_ID)
    .replace('CLIENT_SECRET', CLIENT_SECRET)
    .replace('LATLON', position.coords.latitude +
        ',' + position.coords.longitude), function(result, status) {

			if (status !== 'success') return alert('Request to Foursquare failed');

			console.log(result);
			$("#loc").val(result.response.groups[0].items[0].venue.location.city);
			var venues = result.response.groups[0].items;
			
			var count = venues.length;
			x = 0;
			randomNum = [];
			while(x!=3){
				indexNum = Math.floor(Math.random() * count);
				if($.inArray(indexNum,randomNum)==-1){
					randomNum.push(indexNum);
					x++;
				}
			}
			
			
			// Transform each venue result into a marker on the map.
			for (var i = 0; i < randomNum.length; i++) {
			var venue = venues[randomNum[i]].venue;
			console.log(venue);
			var latlng = L.latLng(venue.location.lat, venue.location.lng);
			var marker = L.marker(latlng)
			.bindPopup('<h2><a href="https://foursquare.com/v/' + venue.id + '">' +
			venue.name + '</a></h2>')
			.addTo(foursquarePlaces);
		}

	});
	

}

/*function showPosition(position){
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
	});*/
	
	/*$.get('functions/fourSquare.php',{'lat': position.coords.latitude,'lon':position.coords.longitude},function(userdata){
		user_array = jQuery.parseJSON(userdata);
		
		size = 0;
		for(i in user_array)
			size++;
			
		x = 0;
		randomNum = [];
		while(x!=3){
			indexNum = Math.floor(Math.random() * size);
			if($.inArray(indexNum,randomNum)==-1){
				randomNum.push(indexNum);
				x++;
			}
		}
		
		for(i in randomNum){
			console.log(user_array[randomNum[i]].location['lat']);
			console.log(user_array[randomNum[i]].location['lng']);
		}
	});
}*/