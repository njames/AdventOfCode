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
    $o2rate = 0;
    $co2rate = 0;

// import the data into an array - drop the new lines and trust php to convert to ints when required :)
//    $data = file('../../input/day03/input03-test.txt', FILE_IGNORE_NEW_LINES); // validate with the test data
$data = file('../../input/day03/input03.txt', FILE_IGNORE_NEW_LINES);


    $numRows = count($data);
    $bits = strlen($data[0]);
echo " rows {$numRows} bits {$bits} " . PHP_EOL;

//set up $totalBitCounts
for ($i = 0; $i< $bits; $i++){
    $totalBitCounts[] = 0;
}

for ($i = 0; $i < $numRows; $i++) {
    $binaryDigits = $binaryData[] = bindec($data[$i]);

//    echo " $binaryDigits  $data[$i] " .PHP_EOL; ///

    // and with 1 to count the bit in RHS and bit shift
    for ($j = 0; $j < $bits; $j++) {
        $totalBitCounts[$j] += ($binaryDigits & 1);
        $binaryDigits = $binaryDigits >> 1;
    }

}
    //    var_dump($totalBitCounts);
    // now that we have counted all the rows we can work out which bits should go where
    // if the number of 1's is > half the total rows it is a one
    // we will do in reverse order and bit shift to the left

    for ($k = $bits; $k > 0; $k-- ) {
       $bit = ( $totalBitCounts[$k - 1] > ($numRows / 2)) ? '1' : '0';

       // concatenate these as strings and then use bindec for multiplication
       $gammaRate .= $bit;
       $epsilonRate .= ($bit === '1' ? '0' : '1');

    }

    echo "Gamma $gammaRate Epsilon $epsilonRate " . PHP_EOL;


    // get the bits from the gamma rate to calulate the 02 rate


//    output the distance
echo 'Part 1: ' . bindec($gammaRate) * bindec($epsilonRate) . PHP_EOL;
//echo 'Part 2: ' . $distance * $depth_2 . PHP_EOL;