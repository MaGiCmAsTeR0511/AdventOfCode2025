<?php
$input = file_get_contents("./AdventodCode2_2");

$splitted = explode(",",$input);

$sum = 0;
foreach($splitted as $key => $value){
    $parts = explode("-",$value);
    for($i = $parts[0]; $i<= $parts[1]; $i++) {
        $s_i = (string)$i;
        $len_i = strlen($s_i);

        for ($sub_len = 1; $sub_len <= $len_i / 2; $sub_len++) {
            if ($len_i % $sub_len == 0) {
                $sub = substr($s_i, 0, $sub_len);
                $repeats = $len_i / $sub_len;
                if (str_repeat($sub, $repeats) === $s_i) {
                    $sum += $i;
                    break; 
                }
            }
        }
    }
}
echo print_r($sum,TRUE)."\n";

?>
