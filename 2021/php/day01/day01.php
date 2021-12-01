<?php

    // set up some vars
    $rises = 0;
    $rises_2 = 0;
    $last_ping = 0;

    // import the data into an array - drop the new lines and trust php to convert to ints when required :)
//    $data = file('../../input/day01/input01-test1.txt', FILE_IGNORE_NEW_LINES); // validate with the test data
    $data = file('../../input/day01/input01-1.txt', FILE_IGNORE_NEW_LINES);


    $pings = count($data) - 1;
    // iterate the array and count the instances of n+1 > N
    for($i = 0; $i < $pings; $i++ ) {
        if ((int)$data[$i] < (int)$data[$i + 1]) {
            $rises = $rises + 1;
        }

        // part 2
        if ($i + 3 <= $pings) {
            $sum1 = array_sum(array_slice($data, $i, 3));
            $sum2 = array_sum(array_slice($data, $i + 1, 3));

            if ($sum2 > $sum1 ){
                $rises_2++;
            }
        }
    }

//    output the count
    echo 'Part 1: ' . $rises . PHP_EOL;
    echo 'Part 2: ' . $rises_2 . PHP_EOL;