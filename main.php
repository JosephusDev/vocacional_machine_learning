<?php
$vetor = [14, 1, 15, 1, 1, 15, 15, 15, 0, 0, 0, 14, 14, 0, 0, 0];
$vetor_str = implode(',', $vetor);

$url = "https://josephus123.pythonanywhere.com/classificar?vetor=$vetor_str";

$response = file_get_contents($url);
$data = json_decode($response, true);

print_r($data);
?>
