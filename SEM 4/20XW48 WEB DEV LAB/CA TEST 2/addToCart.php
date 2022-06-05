<?php
session_start();
$item = array($_POST['name'], $_POST['price'], $_POST['qty']);
array_push($_SESSION['cart'], $item);
header("Location: /SEM 4/20XW48 WEB DEV LAB/CA TEST 2/index.php");
?>