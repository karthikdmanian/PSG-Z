<?php
$servername = "10.1.67.156"; 
$username = "msc20pw16"; 
$password = "msc20pw"; 
$db = 'msc20pw16'; 

// Create connection
$conn = mysqli_connect($servername, $username, $password, $db);
// Check connection
if (!$conn) {
die("Connection failed: " . mysqli_connect_error());
}

//TABLE CREATION
// $sql = "CREATE TABLE student(id INT(6) PRIMARY KEY,name VARCHAR(30) NOT
NULL)";
// if(mysqli_query($conn,$sql)){
// echo 'table created successfully';
// }else{
// echo 'error creating table';
// }

//TABLE INSERTION
// $quer1 = "INSERT INTO student values(1,'abc');";
// $quer1 .= "INSERT INTO student values(2,'xyz');";
// $quer1 .= "INSERT INTO student values(3,'pqr');";
// $quer1 .= "INSERT INTO student values(4,'rst');";
// $quer1 .= "INSERT INTO student values(5,'uvw');";
// $quer1 .= "INSERT INTO student values(6,'xyz');";
// if(mysqli_multi_query($conn,$quer1)){
// echo 'inserted successfully';
// }else{
// echo 'error inserting';
// }
$sql="SELECT name FROM student;";
$res = mysqli_query($conn,$sql);
if(mysqli_num_rows($res)>0){
$names = array();
while($row = mysqli_fetch_assoc($res)){
array_push($names,$row['name']);
}

echo 'Student Records fetched from database:<br>';
echo implode(', ',$names);
echo "<br>Students record after selection sort:<br>";
echo implode(', ',selection_sort($names));
}else{
echo 'no data found';
}
function selection_sort($data)
{
for($i=0; $i<count($data)-1; $i++) {
$min = $i;
for($j=$i+1; $j<count($data); $j++) {
if(strcmp($data[$j], $data[$min]) < 0){
$min = $j;
}
}
$data = swap_positions($data, $i, $min);
}
return $data;
}
function swap_positions($data1, $left, $right) {
$backup_old_data_right_value = $data1[$right];
$data1[$right] = $data1[$left];
$data1[$left] = $backup_old_data_right_value;
return $data1;
}
?>