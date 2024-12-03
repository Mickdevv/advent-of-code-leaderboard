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
        $errors = 0;
        $direction = 0;

        for($i = 1; $i < count($input); $i++) {
            $diff = $input[$i] - $input[$i-1];

            if (!($diff == 0 || $diff > 3 || $diff < -3)) {
                if ($direction == 0) {
                    $direction = $diff;
                } else {
                    if (!(($direction < 0 && $diff < 0) || ($direction > 0 && $diff > 0))) {
                        $errors++;
                    }
                }
            } else {
                $errors++;
            }
        }

        if ($errors < 2) $safe++;
        if ($errors == 1) echo "$line\n";
    }

    echo $safe;
}

// Example usage
$filename = 'input.txt';
processFile($filename);
