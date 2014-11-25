<?php
header ("Content-type: image/png");

////haal downloadgegevens op

//connect
$host = 'localhost';  
$user = 'c1midgethoen';  
$pass = '12478786';  
$name = 'c1sabstats';
session_start();
$db = mysql_connect($host,$user,$pass);

mysql_select_db($name);

//query
$vannacht = strftime("%Y-%m-%d 00:00:00",time()+(60*60*24));
$eergister = strftime("%Y-%m-%d 00:00:00",time()-(0*60*60*24));
//echo $vannacht . "\n";
//echo $eergister . "\n";

$result = mysql_query("SELECT * FROM sabspeed WHERE time <= '" . $vannacht . "' AND time >= '" . $eergister . "' ORDER BY time ASC LIMIT 288",$db);

////draw graph

//setup canvas
$image = "sabspeedgraph.png";
$im = imagecreatefrompng($image);
$orange = imagecolorallocate ($im,255,200,0);
imagesetthickness( $im, 1 );

//loop trough data
$i = 0;
$left = 20;
$top = 124;
while ($set = mysql_fetch_object($result))  {
    $i++;
    if(!($set->speed == 0)){
        $value = $top - ($set->speed)/10;
        $x = $left + $i;
        imageline( $im, $x, $top, $x, $value, $orange );
    }
//    echo $set->time . " " . $set->speed . "\n";
}
imagepng($im);
?>