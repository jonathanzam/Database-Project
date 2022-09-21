<html>
<body>
<h3>Enter a team name to view their results:</h3>

<form action="python_viewResultsTeam.php" method="post">
    Team Name: <input type="text" name="teamName"><br>
    <input name="submit" type="submit" >
</form>
<a href="mainPage.html"><button>Back</button></a>
<br><br>

</body>
</html>

<?php
if (isset($_POST['submit']))
{
    $teamName = escapeshellarg($_POST[teamName]);

    $command = 'python3 python_db.py 5 ' . $teamName;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    //echo "<p>command: $command <p>"; 

    //redirect error output
    $command = $command . " 2>&1";

    // run insert_new_item.py
    echo system($command);     
}
?>