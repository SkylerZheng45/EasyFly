<?php 

$servername = "localhost";
$username = "root";
$password = "abinav2019$";

$city = "Austin";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";

$result = mysql_query("SELECT code FROM airports WHERE city='$city'");

$row = mysql_fetch_array($result);









?>