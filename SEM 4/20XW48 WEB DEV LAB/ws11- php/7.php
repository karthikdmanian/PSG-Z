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
        function check_palindrome($string) 
        {
        if ($string == strrev($string))
            return "YES";
        else
            return "NO";
        }
        echo check_palindrome('madam')."<br>";
        echo check_palindrome('nurses');

    ?>
</body>
</html>