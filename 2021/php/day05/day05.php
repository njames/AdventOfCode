<?php


// set up some vars
$points = [];


// import the data into an array - drop the new lines and trust php to convert to ints when required :)
    $data = file_get_contents('../../input/day05/input05-test.txt'); // validate with the test data
//$data = file('../../input/day05/input05.txt', FILE_IGNORE_NEW_LINES);

// read each line and split into points
$points = explode(PHP_EOL, $data);

//var_dump($points);
foreach ($points as $p){
//    $point;
    preg_match_all("(d\,d)\ \-\>\ (d\, d)", $p, $point );

    var_dump($point);
}