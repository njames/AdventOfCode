<?php


// set up some vars
$bits = 0;
$totalBitCounts = [];
$binaryData = [];
$andTotal = 0;
$xorTotal = 0;
$orTotal = 0;
$gammaRate = '';
$epsilonRate = '';
$o2rate = '';
$co2rate = '';

// import the data into an array - drop the new lines and trust php to convert to ints when required :)
//    $data = file('../../input/day05/input05-test.txt', FILE_IGNORE_NEW_LINES); // validate with the test data
$data = file('../../input/day05/input05.txt', FILE_IGNORE_NEW_LINES);

