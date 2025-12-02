<?php
$input = file_get_contents("./AdventodCode2_1");

$splitted = explode(",",$input);

$sum = 0;
foreach($splitted as $key => $value){
    $parts = explode("-",$value);
    for($i = $parts[0]; $i<= $parts[1]; $i++) {

        $length1 = strlen($i);
        if($length1 % 2 == 0) {
            if (substr($i, 0, $length1 / 2) == substr($i, $length1 / 2, $length1)) {
                $sum += $i;
            }
        }
    }
}
echo print_r($sum,TRUE)."\n";








?>
