<?php

/**
 * Findet die lexikographisch größte Teilsequenz einer bestimmten Länge.
 *
 * @param string $number_str Die ursprüngliche Zeichenkette aus Ziffern.
 * @param int $k Die gewünschte Länge der Teilsequenz.
 * @return string Die größte gefundene Teilsequenz.
 */
function findLargestJoltage($number_str, $k) {
    $result = '';
    $current_pos = 0;
    $number_len = strlen($number_str);

    // Wir müssen k Ziffern auswählen.
    for ($i = 0; $i < $k; $i++) {
        // Bestimme das Suchfenster für die aktuelle Ziffer.
        // Wir müssen am Ende genügend Ziffern für die restlichen Auswahlen übrig lassen.
        $needed_for_rest = $k - 1 - $i;
        $search_end_pos = $number_len - $needed_for_rest;

        $max_digit = -1;
        $max_pos = -1;

        // Finde die größte Ziffer im aktuellen Fenster [current_pos, search_end_pos).
        for ($j = $current_pos; $j < $search_end_pos; $j++) {
            if ($number_str[$j] > $max_digit) {
                $max_digit = $number_str[$j];
                $max_pos = $j;
            }
        }

        // Füge die beste gefundene Ziffer an das Ergebnis an.
        $result .= $max_digit;

        // Die nächste Suche muss nach der Position der gerade gefundenen Ziffer beginnen.
        $current_pos = $max_pos + 1;
    }

    return $result;
}

$handle = fopen("./AdventodCode3_2", "r");
if (!$handle) {
    die("Konnte die Datei AdventodCode3_2 nicht öffnen");
}

$summe = '0';
$joltage_length = 12;

while (($line = fgets($handle)) !== false) {
    $line = trim($line);
    $largest_joltage = findLargestJoltage($line, $joltage_length);
    // bcadd wird für die Addition von großen Zahlen als Strings verwendet.
    $summe = bcadd($summe, $largest_joltage);
}

fclose($handle);

echo $summe . "\n";

?>
