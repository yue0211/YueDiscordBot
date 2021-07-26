<?php 

$text= $_POST["text"];
// data strored in array

$Json = file_get_contents("setting.json");
// Converts to an array 
$myarray = json_decode($Json, true);


//echo $text;
$result="";

for($i=0;$i<count($myarray["id"]);$i++)
	if($myarray["id"][$i]==$text)
	{
		for($j=0;$j<10;$j++)
		  $result=$result.strval(rand(0,10));
		break;
	}
	
echo "驗證碼:".$result;

$myarray["code"]=$result;


// encode array to json
$json = json_encode($myarray);
$bytes = file_put_contents("setting.json", $json); 

?>