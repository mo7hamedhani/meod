<?php $your_visitor_ip_address = $_SERVER['REMOTE_ADDR'];                          
$get_data = file_get_contents('http://www.geoplugin.net/php.gp?ip='.$your_visitor_ip_address);                          
$get_all_data_list = unserialize($get_data);                          
$country = $get_all_data_list['geoplugin_countryName'];                          
$city = $get_all_data_list['geoplugin_city'];                          
$continent = $get_all_data_list['geoplugin_continentName'];                          
$currency_exchange = $get_all_data_list['geoplugin_currencyConverter'];                          
$region = $get_all_data_list['geoplugin_region'];                          
$regionCode = $get_all_data_list['geoplugin_regionCode'];                          
$regionName = $get_all_data_list['geoplugin_regionName'];                          
$countryCode = $get_all_data_list['geoplugin_countryCode'];                          
$continentCode = $get_all_data_list['geoplugin_continentCode'];                          
$latitude = $get_all_data_list['geoplugin_latitude'];                          
$dmaCode = $get_all_data_list['geoplugin_dmaCode'];                          
$inEU = $get_all_data_list['geoplugin_inEU'];                          
$euVATrate = $get_all_data_list['geoplugin_euVATrate'];                          
$longitude = $get_all_data_list['geoplugin_longitude'];                          
$currencyCode = $get_all_data_list['geoplugin_currencyCode'];                          
$currencySymbol = $get_all_data_list['geoplugin_currencySymbol'];                          
$locationAccuracyRadius = $get_all_data_list['geoplugin_locationAccuracyRadius'];                          
$timezone = $get_all_data_list['geoplugin_timezone'];          ?>

 <?php echo $currencyCode; ?> 