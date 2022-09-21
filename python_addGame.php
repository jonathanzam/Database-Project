<html>
<body>
<h3>Enter information about a game to add to the database:</h3>

<form action="python_addGame.php" method="post">
    Game ID: <input type="text" name="gameID"><br>
    Game Location: <input type="text" name="gameLocation"><br>
    Game Date [MM/DD/YY]: <input type="text" name="gameDate"><br>
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
    $gameLocation = escapeshellarg($_POST[gameLocation]);
    $gameDate = escapeshellarg($_POST[gameDate]);

    $command = 'python3 python_db.py 2 ' . $gameID . ' ' . $gameLocation . ' ' . $gameDate;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    //echo "<p>command: $command <p>"; 

    //redirect error output
    $command = $command . " 2>&1";

    // run insert_new_item.py
    echo system($command);     
}
?>