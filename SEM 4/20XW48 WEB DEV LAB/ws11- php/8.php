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
        echo "
        Associative array : Ascending order sort by value
        <br>";
        $array2=array("Sophia"=>"31","Jacob"=>"41","William"=>"39","Ramesh"=>"40"); 
        
        // sorts in Ascending order
        asort($array2);
        foreach($array2 as $y=>$y_value)
        {
        echo "Age of ".$y." is : ".$y_value."
        ";
        }
        echo "
        <br>Associative array : Ascending order sort by Key
        <br>";
        $array3=array("Sophia"=>"31","Jacob"=>"41","William"=>"39","Ramesh"=>"40"); 

        // ascending sort but wrto key
        ksort($array3);
        foreach($array3 as $y=>$y_value)
        {
        echo "Age of ".$y." is : ".$y_value."
        ";
        }
        echo "
        <br>Associative array : Descending order sorting by Value
        <br>";
        $age=array("Sophia"=>"31","Jacob"=>"41","William"=>"39","Ramesh"=>"40");

        // sort in descending
        arsort($age);
        foreach($age as $y=>$y_value)
        {
        echo "Age of ".$y." is : ".$y_value."
        ";
        }
        echo "
        <br>Associative array : Descending order sorting by Key
        <br>";
        $array4=array("Sophia"=>"31","Jacob"=>"41","William"=>"39","Ramesh"=>"40"); 
        

        // sort in descending according to the key
        krsort($array4);
        foreach($array4 as $y=>$y_value)
        {
        echo "Age of ".$y." is : ".$y_value."
        ";
        } 
    ?>
</body>
</html>