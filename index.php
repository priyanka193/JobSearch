<!DOCTYPE html>
<html>
<head>
	<title>Job Portal</title>
</head>
<body>
<h1>First heroku app</h1>

<?php

	$dbh = pg_connect("host='ec2-54-243-185-132.compute-1.amazonaws.com' dbname='d2ftjp5a24rakj' user='bgcdtjsazvveou' password='b8288eda378a650ad70687aff55ac3bdcd0f73dc634bc5f3a6a63847b4259308'");
	if(!$dbh)
	{
		die("error".pg_last_error());
	}
	$sql = "SELECT * FROM job_type";
	$result = pg_query($dbh,$sql);
	if(!$result)
	{
		die("error".pg_last_error());
	}
	while($row = pg_fetch_array($result))
	{
		echo "Type:".$row[0]."</br>";
		echo "Description:".$row[1]."</br>";
	}
	pg_free_result($result);
	pg_close($dbh);
?>

<?

/*$dbopts = parse_url(getenv('DATABASE_URL'));
$app->register(new Herrera\Pdo\PdoServiceProvider(),
               array(
                   'pdo.dsn' => 'pgsql:dbname='.ltrim($dbopts["path"],'/').';host='.$dbopts["host"] . ';port=' . $dbopts["port"],
                   'pdo.username' => $dbopts["user"],
                   'pdo.password' => $dbopts["pass"]
               )
);
*/
?>
</body>
</html>
