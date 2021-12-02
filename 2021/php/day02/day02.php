<?php

    // set up some vars
    $depth = 0;
    $distance = 0;
    $aim = 0; //  

// lets use a PHP8.1 enum :)
    enum Steering: string
    {
        case forward = 'forward';
        case up = 'up';
        case down = 'down';
    }

    // import the data into an array - drop the new lines and trust php to convert to ints when required :)
//    $data = file('../../input/day02/input02-test1.txt', FILE_IGNORE_NEW_LINES); // validate with the test data
    $data = file('../../input/day02/input02-1.txt', FILE_IGNORE_NEW_LINES);

    $directions = count($data);

//    echo $directions . PHP_EOL;

    // used these to get the hang of enums
//    echo Steering::down->name .PHP_EOL;
//    echo Steering::down->value . PHP_EOL;


    // iterate the array and add to the direction forward or up / down
    for($i = 0; $i < $directions; $i++ ) {
        $direction = explode(' ', $data[$i]);

//        var_dump($direction);

        switch ($direction[0]) {
            case Steering::down->value:
               $depth += (int)$direction[1];
               break;
            case Steering::up->value:
                $depth -= (int)$direction[1];
                break;
            case Steering::forward->value:
                $distance += (int)$direction[1];
                break;
            default:
                echo "nothing matched {$distance[0]}  {$distance[1]} " . PHP_EOL;

        }
//        echo "Current position {$distance} current depth {$depth}" .PHP_EOL;
    }

//    output the distance
    echo 'Part 1: ' . $distance * $depth . PHP_EOL;
//    echo 'Part 2: ' . $rises_2 . PHP_EOL;