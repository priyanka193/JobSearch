<!DOCTYPE html>
<html>
<head>
	<title>Blah</title>
</head>
<body>
<h1>First heroku app</h1>

<?php

	$dbh = pg_connect("host= dbname= user= ");
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
