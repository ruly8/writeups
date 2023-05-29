<?php 
header("Access-Control-Allow-Origin: http://localhost:8080");
header("Access-Control-Allow-Credentials: true");
$codepoint = "\u{d800}";
header("Set-Cookie: $codepoint=php localhost set-cookie header; SameSite=None; Secure");
$stdout = fopen('php://stdout', 'w');
$c = var_export($_COOKIE, true);
fwrite($stdout, $c . "\n");
for ( $pos=0; $pos < strlen($codepoint); $pos++ ) {
    $byte = substr($codepoint, $pos);
    echo 'Byte ' . $pos . ' has value ' . ord($byte) . PHP_EOL;
}
var_dump(mb_ord($codepoint, "UTF-16"));
?>

<html>
<head>
<title>PHP Test</title>
</head>
<body>
<p id="demo"></p>
<?php 
var_dump($_COOKIE);
var_dump($_SERVER["HTTP_COOKIE"]);
echo '<script>
document.getElementById("demo").innerHTML = document.cookie;
</script>';
?>
</body>
</html>
