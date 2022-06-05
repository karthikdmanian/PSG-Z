<html lang="en">
<body>
<p>
<?php
$mails = array('20pw38@psgtech.ac.in', 'A@b@c@domain.com',

'example@domain.com', 'abc\is\”not\valid@domain.com');
for($i=0; $i < count($mails); $i++){
if(filter_var($mails[$i], FILTER_VALIDATE_EMAIL)){
echo $mails[$i].': Valid email address<br>';
}
else{
echo $mails[$i].': Invalid email address<br>';
}
}
?>
</p>
</body>
</html>