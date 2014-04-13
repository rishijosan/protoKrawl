<?php
	$lat = $_GET['lat'];	
	$lon = $_GET['lon'];
	$url  = "http://maps.googleapis.com/maps/api/geocode/json?latlng=".$lat.",".$lon."&sensor=false";
	$curl = curl_init($url);	
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);                         
	curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_ANY);                                          
	curl_setopt($curl, CURLOPT_USERAGENT, 'Sample Code');
	$response = curl_exec($curl);                                          
	$resultStatus = curl_getinfo($curl);                                   
	if($resultStatus['http_code'] == 200){
		echo $response;
	}
?>