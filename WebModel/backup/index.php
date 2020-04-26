<?php

// Receive the parameters from client side

// lotsize	bathrms	driveway	recroom	fullbase	
// gashw	airco	garagepl	prefarea	stories_four	
// stories_one	stories_three

// a. Get Lotsize information = http://www.hackveda.in/sistec/Housing_Modifed.csv
$lotsize = $_GET["lotsize"];
$bathrooms = $_GET["bathrms"];
$driveway = $_GET["driveway"];
$recroom = $_GET["recroom"];
$fullbase = $_GET["fullbase"];
$gashw = $_GET["gashw"];
$airco = $_GET["airco"];
$garagepl = $_GET["garagepl"];
$prefarea = $_GET["prefarea"];
$stories_four = $_GET["stories_four"];
$stories_one = $_GET["stories_one"];
$stories_three = $_GET["stories_three"];

// Post Requests
$lotsize = $_POST["lotsize"];
$bathrooms = $_POST["bathrms"];
$driveway = $_POST["driveway"];
$recroom = $_POST["recroom"];
$fullbase = $_POST["fullbase"];
$gashw = $_POST["gashw"];
$airco = $_POST["airco"];
$garagepl = $_POST["garagepl"];
$prefarea = $_POST["prefarea"];
$stories_four = $_POST["stories_four"];
$stories_one = $_POST["stories_one"];
$stories_three = $_POST["stories_three"];


// b. send the information to test_model.py
system("/usr/bin/python3 house_model.py ".$lotsize." ".$bathrooms." ".$driveway." ".
$recroom." ".$fullbase." ".$gashw." ".$airco." ".$garagepl." ".$prefarea." ".$stories_four." ".
$stories_one." ".$stories_three." 2<&1");

?>
