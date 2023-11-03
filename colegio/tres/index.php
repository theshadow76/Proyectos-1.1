<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php 
        $command = "python3 app.py";
        $pid = popen( $command,"r");
        while( !feof( $pid ) )
        {
            echo fread($pid, 256);
            flush();
            ob_flush();
            usleep(100000);
        }
        pclose($pid);
    ?>
</body>
</html>