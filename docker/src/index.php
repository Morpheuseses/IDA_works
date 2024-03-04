<?php

    $server = new \PDO("mysql:host=localhost;dbname=Pryazha;", 'root', 'EmPelmeny123');
    if ($server) {
        echo "Hello";
    }
?>