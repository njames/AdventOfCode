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
//    $data = file('../../input/day03/input03-test.txt', FILE_IGNORE_NEW_LINES); // validate with the test data
$data = file('../../input/day03/input03.txt', FILE_IGNORE_NEW_LINES);


    $numRows = count($data);
    $bits = strlen($data[0]);
echo " rows {$numRows} bits {$bits} " . PHP_EOL;

//set up $totalBitCounts // haha - use array_pad !
$totalBitCounts = array_pad($totalBitCounts, $bits, 0);

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

    $o2Result = $data;
    $co2Result = $data;

    // get the bits from the gamma rate to calculate the 02 rate and co2 rate
    for ( $k = 0 ; $k < $bits && count($o2Result) > 1; $k++) {
        $o2Result = reduce_array($o2Result, $k, $gammaRate[$k], 1);

        var_dump($o2Result);
        echo'-------------------------';
    }

    for ( $k = 0 ; $k < $bits && count($co2Result) > 1; $k++){
        $co2Result = reduce_array($co2Result, $k, $epsilonRate[$k], 0);
    }

    var_dump($o2Result);
//    output the distance
echo 'Part 1: ' . bindec($gammaRate) * bindec($epsilonRate) . PHP_EOL;
echo 'Part 2: ' . bindec($o2Result[0]) * bindec($co2Result[0]). PHP_EOL;


function reduce_array($array, $pos, $checkDigit, $keepIfEven){

    $result = ['0' => [], '1' => []];

    foreach ($array as $row) {
        if($row[$pos] === $checkDigit) {
            $result[$checkDigit][] = $row;
        }else{
            $otherDigit = ($checkDigit === '1') ? '0' : '1';
            $result[$otherDigit][] = $row;
        }
    }

    if( count($result[0]) === count($result[1]))
        return $result[(int)$keepIfEven];
    else
        return $result[(int)$checkDigit];

}