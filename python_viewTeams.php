<html>
<body>
<h3>View all teams information:</h3>

<form action="python_viewTeams.php" method="post">
</form>
<a href="mainPage.html"><button>Back</button></a>
<br><br>

</body>
</html>

<?php
#$if (isset($_POST['submit']))
{
    $command = 'python3 python_db.py 4';

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    //echo "<p>command: $command <p>"; 

    //redirect error output
    $command = $command . " 2>&1";

    // run insert_new_item.py
    echo system($command);     
}
?>