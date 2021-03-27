<?php
$data=json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"));
$key="qw8J";
$cookie="";
for($i=0;$i<strlen($data);$i++){
  $cookie.=$data[$i]^$key[$i%strlen($key)];
} 
print(base64_encode($cookie));
?>
