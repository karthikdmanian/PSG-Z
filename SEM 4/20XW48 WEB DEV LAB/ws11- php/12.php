<html>
<body>
<?php
function fun1($a){
return substr($a, -3) == "xas";
}
function fun2($a){

return strcasecmp(substr($a, 0, 1),'k')==0 &&

strcasecmp(substr($a, -1, 1),'s')==0;
}
function fun3($a){
return substr($a, 0, 1) == 'M' && substr($a, -1, 1) =='s';
}
function fun4($a){
return substr($a, -1, 1) =='a';
}
function fun5($a){
return substr($a, 0, 1) =='M';
}
$states = "Mississippi Texas Alabama Massachusetts Kansas";
$statesArray = array();
$statesArray = array_merge($statesArray, array_filter(explode('

', $states), 'fun1'));

$statesArray = array_merge($statesArray, array_filter(explode('

', $states), 'fun2'));

$statesArray = array_merge($statesArray, array_filter(explode('

', $states), 'fun3'));

$statesArray = array_merge($statesArray, array_filter(explode('

', $states), 'fun4'));

array_push($statesArray, array_filter(explode(' ', $states),

'fun5')[0]);

print_r($statesArray);
?>
<p>
</p>
</body>
</html>