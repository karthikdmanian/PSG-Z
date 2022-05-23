
<?php
	
	$host = '10.1.67.156';
	$name = 'msc20pw16';
	$pass = 'msc20pw';
	$db = 'msc20pw16';
	
	$conn = mysqli_connect($host, $name, $pass, $db);
	// Check connection
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
  	}
  	echo "Connected to database msc20pw16!";
	 

	// // Table creation 
	// $sql = "CREATE TABLE Products (
	// 	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	// 	pName VARCHAR(30) NOT NULL,
	// 	pDescription VARCHAR(255) NOT NULL,
	// 	pPrice FLOAT
	// 	);";
	
	// if (mysqli_query($conn, $sql)) {
	// 	echo "\nTable Products created successfully";
	// } else {
	// 	echo "Error creating table: " . mysqli_error($conn);
	// }


	
  ?>

<?php
session_start();
if(!isset($_SESSION['cart'])){
$_SESSION['cart'] = array();
}
?>


<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Seafood Order Form</title>
</head>
<body style="background: #E9D5CA">
    <div style="display: flex">
        <form action="viewCart.php" >
        <input type="submit" value="View Cart">
        </form>
        <form action="deleteCart.php" method="post">
        <input type="submit" value='Delete Cart'>
        </form>
    </div>
    
    <div style="display: flex">
        <div>
            <div>
            <h1>Salmon</h1>
            <h2>₹ 15.99</h2>
            <img src="https://formfacade.com/uploaded/1FAIpQLSc-gauOSBL3Jjawo8rx8s3C5WyY3Ii_4Gld_7IvO0FavAbJUg/2090491919/prdimage/Salmon.jpg" alt="" height="250" width="250">
            </div>
            <form action="addToCart.php" method="POST">
            <input type="hidden" name="name" value="Salmon">
            <input type="hidden" name="price" value="15.99">
            <input type="number" name="qty">
            <input type="submit" value="Add to Cart">
            </form>
        </div>

        <div>
            <div>
            <h1>Sea Bass</h1>
            <h2>₹ 39.50</h2>
            <img src="https://formfacade.com/uploaded/1FAIpQLSc-gauOSBL3Jjawo8rx8s3C5WyY3Ii_4Gld_7IvO0FavAbJUg/629992681/prdimage/Sea%20bass.jpg" alt="" height="250" width="250">
            </div>
            <form action="addToCart.php" method="POST">
            <input type="hidden" name="name" value="Sea Bass">
            <input type="hidden" name="price" value="39.50">
            <input type="number" name="qty">
            <input type="submit" value="Add to Cart">
            </form>
        </div>

    </div>
    
    <div style="display: flex">
        <div>
            <div>
            <h1>Trout</h1>
            <h2>₹ 15.75</h2>
            <img src="https://formfacade.com/uploaded/1FAIpQLSc-gauOSBL3Jjawo8rx8s3C5WyY3Ii_4Gld_7IvO0FavAbJUg/852727129/prdimage/Trout.jpg" alt="" height="250" width="250">
            </div>
            <form action="addToCart.php" method="POST">
            <input type="hidden" name="name" value="Trout">
            <input type="hidden" name="price" value="15.75">
            <input type="number" name="qty">
            <input type="submit" value="Add to Cart">
            </form>
        </div>

        <div>
            <div>
            <h1>Prawn</h1>
            <h2>₹ 22.99</h2>
            <img src="https://formfacade.com/uploaded/1FAIpQLSc-gauOSBL3Jjawo8rx8s3C5WyY3Ii_4Gld_7IvO0FavAbJUg/1845944743/prdimage/Prawn.jpg" alt="" height="250" width="250">
            </div>
            <form action="addToCart.php" method="POST">
            <input type="hidden" name="name" value="Prawn">
            <input type="hidden" name="price" value="22.99">
            <input type="number" name="qty">
            <input type="submit" value="Add to Cart">
            </form>
        </div>
    </div>
    
</body>
</html>