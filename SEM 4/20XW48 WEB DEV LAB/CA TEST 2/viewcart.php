<?php
session_start();
$sum=0;
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Document</title>
</head>
<body>
    <table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Quantity</th>
    </tr>
    <?php
        foreach($_SESSION['cart'] as $item){
        echo '<tr>';
        echo '<td>'.$item[0].'</td>';
        echo '<td>'.$item[1].'</td>';
        echo '<td>'.$item[2].'</td>';
        echo '</tr>';
        $sum=$sum+($item[1]*$item[2]);
        }
       
    ?>
    </table>
    <?php
         echo "<br><br>The Total:";
         echo $sum;
    ?>
</body>
</html>