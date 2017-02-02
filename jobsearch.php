<!DOCTYPE html>
<html>
<head>
	<title>Job Search</title>
</head>
<body>
<?php
	DEFINE('DB_USER','root');
	DEFINE('DB_PASSWORD','');
	DEFINE('DB_HOST','localhost');
	DEFINE('DB_NAME','JOBSEARCH');
	$dbc = @mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die('Could not connect to MySQL: '.mysqli_connect_error());
	mysqli_set_charset($dbc,'utf8');

	$q = "SELECT * FROM JOB_SEARCH_RESULTS";
	$r = @mysqli_query($dbc,$q);
	if($r)
	{
		while($value = mysqli_fetch_array($r,MYSQLI_ASSOC))
		{
			echo "</br>Job Title:\e".$value["job_title"]."</br>Company:\e".$value["company"]."</br>Snippet:".$value["snippet"]."</br>Location:".$value["location"]."</br>Url:<a target='_blank' href='".$value["url"]."'>Indeed Link</a>"."</br>Posted:".$value["time_posted"]."</br></p><hr>";
		}
	}
/*	$file = 'jobs.json';
	$json = json_decode(file_get_contents($file),TRUE);
	

	foreach ($json as $key => $value) {

		$jobtitle = $value["jobtitle"];
		$company = $value["company"];
		$snippet = $value["snippet"];
		$location = $value["formattedLocationFull"];
		$url = $value["url"];
		$posted = $value["formattedRelativeTime"];


		echo "</br>Job Title:\e".$value["jobtitle"]."</br>Company:\e".$value["company"]."</br>Snippet:".$value["snippet"]."</br>Location:".$value["formattedLocationFull"]."</br>Url:<a href='".$value["url"]."'>Indeed Link</a>"."</br>Posted:".$value["formattedRelativeTime"]."</br></p><hr>";


		$query = "INSERT INTO JOB_SEARCH_RESULTS (job_search_id, participant_id, url, company, location, time_posted, job_title, snippet) VALUES (NULL, '','$url','$company','$location','$posted','$jobtitle', '$snippet')";
		$run_query = @mysqli_query($dbc, $query);

	}
*/


	

/*	$q = "SELECT * FROM JOB_TYPE";
	$q1 = "SELECT * FROM PARTICIPANT";
	$count = 1;
	$w1 = @mysqli_query($dbc,$q1);
	$r = @mysqli_query($dbc,$q);
	if($w1)
	{
		while($row = mysqli_fetch_array($r,MYSQLI_ASSOC))
		{
			echo '<p>'.$row['type_description'].'</p>';
		}
	}
*/

?>
</body>
</html>