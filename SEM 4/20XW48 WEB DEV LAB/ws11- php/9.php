<?php
session_start();
if(!isset($_SESSION['bg'])){
$_SESSION['bg'] = 'white';
}
if(!isset( $_SESSION['fg'])){
$_SESSION['fg'] = 'black';
}
?>
<html>
<head><title>Document</title></head>
<body bgcolor="<?= $_SESSION['bg'] ?>" text="<?= $_SESSION['fg'] ?>">
Not a fan of the theme? <a href="prefs.html" style='color:
<?=$_SESSION['fg'] ?>;' >Change your preferences?</a>
</body>
</html>