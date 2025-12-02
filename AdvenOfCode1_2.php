<?php
$handle = fopen ("./AdventodCode1_2","r");
$count = [];
$number = 50;
while ( $inhalt = fgets($handle, 4096 ))
{
    $length = strlen($inhalt);
    switch(substr($inhalt,0,1)){
        case 'L':
            $number = $number - (int)substr($inhalt ,1,$length);
            break;
        case 'R':
            $number = $number +(int)substr($inhalt,1,$length);
            break;
    }
    $currentPosition = (($number % 100) + 100) % 100;
    array_key_exists($currentPosition,$count) ? $count[$currentPosition]++ : $count[$currentPosition] = 1;
}
$max = [];

echo print_r($count,TRUE)."\n";
echo print_r((max($count)),TRUE)."\n";
?>
