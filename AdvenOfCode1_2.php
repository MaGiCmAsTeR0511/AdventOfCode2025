<?php
$handle = fopen("./AdventodCode1_2", "r");
if ($handle) {
    // Das Ziffernblatt startet bei 50. Wir verfolgen die Position auf einer unendlichen Achse.
    $unbounded_pos = 50;
    $zero_count = 0;

    while (($line = fgets($handle)) !== false) {
        $line = trim($line);
        if (empty($line)) {
            continue;
        }

        $direction = substr($line, 0, 1);
        $value = (int)substr($line, 1);

        $start_pos = $unbounded_pos;
        $rotation = 0;

        if ($direction === 'L') {
            $rotation = -$value;
        } else if ($direction === 'R') {
            $rotation = $value;
        }

        if ($rotation === 0) {
            continue;
        }

        $unbounded_pos += $rotation;
        $end_pos = $unbounded_pos;

        $crossings = 0;
        if ($rotation > 0) { // Rechtsdrehung
            // Zähle die Vielfachen von 100 im Intervall (start_pos, end_pos]
            $crossings = floor($end_pos / 100) - floor($start_pos / 100);
        } else { // Linksdrehung
            // Zähle die Vielfachen von 100 im Intervall [end_pos, start_pos)
            $crossings = floor(($start_pos - 1) / 100) - floor(($end_pos - 1) / 100);
        }
        
        $zero_count += $crossings;
    }

    fclose($handle);

    echo "The new password is: " . $zero_count . "\n";
} else {
    echo "Fehler beim Öffnen der Datei.";
}
?>
