<?php
function processFile($filename) {
    if (!file_exists($filename)) {
        die("File not found.");
    }

    $lines = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

    day2($lines);
    // foreach ($lines as $line) {
    //     // Process each line (representing a test)
    //     //echo "Processing: $line\n";
    // }
}

function day2($lines) {
    $safe = 0;

    foreach($lines as $line) {
        $input = explode(' ', $line);
        $flag = true;
        $direction = 0;

        for($i = 1; $i < count($input); $i++) {
            if (!$flag) {continue;}

            $diff = $input[$i] - $input[$i-1];

            if (($diff > 0 && $diff < 4) || ($diff < 0 && $diff > -4)) {
                if ($direction == 0) {
                    $direction = $diff;
                } else {
                    if (($direction < 0 && $diff < 0) || ($direction > 0 && $diff > 0)) {
                        $flag = true;
                    } else {
                        $flag = false;
                    }
                }
            } else {
                $flag = false;
            }
        }

        if ($flag) $safe++;
    }

    echo $safe;
}

// Example usage
$filename = 'input.txt';
processFile($filename);
