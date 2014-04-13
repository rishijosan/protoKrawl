<?php
	//$lat = $_GET['lat'];	
	//$lon = $_GET['lon'];
	
	
	//$lat = 40.5213022;
	//$lon = -74.456815;
	$lat = $_GET['lat'];	
	$lon = $_GET['lon'];
	
	$url = "172.31.217.127:5000/getVenue?lat=".$lat."&lon=".$lon;
		
//	$url  = "http://maps.googleapis.com/maps/api/geocode/json?latlng=".$lat.",".$lon."&sensor=false";
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