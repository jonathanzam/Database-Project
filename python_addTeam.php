<html>
<body>
<h3>Enter information about a team to add to the database:</h3>

<form action="python_addTeam.php" method="post">
    Team Name: <input type="text" name="teamName"><br>
    Team Nickname <input type="text" name="teamNickname"><br>
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
    $teamNickname = escapeshellarg($_POST[teamNickname]);

    $command = 'python3 python_db.py 1 ' . $teamName . ' ' . $teamNickname;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    //echo "<p>command: $command <p>"; 

    //redirect error output
    $command = $command . " 2>&1";

    // run insert_new_item.py
    echo system($command);     
}
?>