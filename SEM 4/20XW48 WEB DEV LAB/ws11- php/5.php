<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<?php
    $month_temp = "78, 60, 62, 68, 71, 68, 73, 85, 66, 64, 76, 63, 81, 76, 73,
    68, 72, 73, 75, 65, 74, 63, 67, 65, 64, 68, 73, 75, 79, 73";

    // picks elt after each ,
    $temp_array = explode(',', $month_temp);
    
    echo "THe array: <br>";
    foreach($temp_array as $temp)
    {
        echo $temp." ";
    }
    echo "<br>";

    // totalling
    $tot_temp = 0;
    $temp_array_length = count($temp_array);
    foreach($temp_array as $temp)
    {
    $tot_temp += $temp;
    }

    // avg temp
    $avg_high_temp = $tot_temp/$temp_array_length;
    echo "Average Temperature is : ".$avg_high_temp. "<br>
    ";
    
    // finding bounds
    sort($temp_array);
    echo " List of five lowest temperatures :<br>";
    for ($i=0; $i< 5; $i++)
    { 
    echo $temp_array[$i].", ";
    }
    echo "<br>List of five highest temperatures :<br>";
    for ($i=($temp_array_length-5); $i< ($temp_array_length); $i++)
    {
    echo $temp_array[$i].", ";
    }
?>
        
</body>
</html>