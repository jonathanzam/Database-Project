<html>
<body>
<h3>Enter information about a game result to add to the database:</h3>

<form action="python_addResult.php" method="post">
    Game ID: <input type="text" name="gameID"><br>
    Team 1 ID: <input type="text" name="teamOneID"><br>
    Team 2 ID: <input type="text" name="teamTwoID"><br>
    Team 1 Score: <input type="text" name="teamOneScore"><br>
    Team 2 Score: <input type="text" name="teamTwoScore"><br>
    <input name="submit" type="submit" >
</form>
<a href="mainPage.html"><button>Back</button></a>
<br><br>

</body>
</html>

<?php
if (isset($_POST['submit']))
{
    $gameID = escapeshellarg($_POST[gameID]);
    $teamOneID = escapeshellarg($_POST[teamOneID]);
    $teamTwoID = escapeshellarg($_POST[teamTwoID]);
    $teamOneScore = escapeshellarg($_POST[teamOneScore]);
    $teamTwoScore = escapeshellarg($_POST[teamTwoScore]);

    $command = 'python3 python_db.py 3 ' . $gameID . ' ' . $teamOneID . ' ' . $teamTwoID . ' ' . $teamOneScore . ' ' . $teamTwoScore;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    //echo "<p>command: $command <p>"; 

    //redirect error output
    $command = $command . " 2>&1";

    // run insert_new_item.py
    echo system($command);     
}
?>