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
        $str1 = 'The quick      " " 	 brown fox';
        // replaces the whitespaces
        echo preg_replace('/\s+/', '', $str1)."\n";
    ?>
</body>
</html>