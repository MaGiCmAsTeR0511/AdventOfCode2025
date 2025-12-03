<?php
$handle = fopen("./AdventodCode3_1","r");
$zahl = [];
$summe = 0;
while( $line = fgets($handle, 4096)){
    $numbers = str_split(trim($line),1);
    if(strpos($line,max($numbers)) === count($numbers)-1){
           $zahl[1]= max($numbers);
           unset($numbers[strpos($line,max($numbers))]);
           $zahl[0] = max($numbers);
           asort($zahl);
    }else {
        $zahl[0] = max($numbers);
        $pos = strpos($line,max($numbers));
        for($i=0;$i<=$pos;$i++){
            unset($numbers[$i]);
        }
        $zahl[1] = max($numbers);
    }

    $summe += (int)implode($zahl);
}

echo print_r($summe ,TRUE)."\n";
?>
