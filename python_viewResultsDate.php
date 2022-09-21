<html>
<body>
<h3>Enter date to view game results:</h3>

<form action="python_viewResultsDate.php" method="post">
    Date [MM/DD/YY]: <input type="text" name="date"><br>
    <input name="submit" type="submit" >
</form>
<a href="mainPage.html"><button>Back</button></a>
<br><br>

</body>
</html>

<?php
if (isset($_POST['submit']))
{
    $date = escapeshellarg($_POST[date]);

    $command = 'python3 python_db.py 6 ' . $date;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    //echo "<p>command: $command <p>"; 

    //redirect error output
    $command = $command . " 2>&1";

    // run insert_new_item.py
    echo system($command);     
}
?>