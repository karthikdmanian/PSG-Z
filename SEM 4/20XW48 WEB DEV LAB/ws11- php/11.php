<?php
if(isset($_POST['setCookie'])){
setcookie('name', $_POST['name'], time()+ 3600, '/');
header('Location: /11.php');
}
?>
<html lang="en">
<head>
<title>Document</title>
</head>
<body>
<?php
if(!isset($_COOKIE['name'])){
echo 'Hello anonymous_user!';
}
else{
echo 'Hello '.$_COOKIE['name'].'!';
}
?>
<form action = '11.php' method='post'>
<input type="text" name='name'>
<input type="submit" name= 'setCookie' value='Set Cookie'>
</form>
</body>
</html>