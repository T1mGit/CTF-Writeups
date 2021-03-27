<?php
function get_key($plain, $crypt)
{
 $key="";
 print("Cleartext Length:".strlen($plain));
 print("\nCiphertext Length:".strlen($crypt));
 for($i=0;$i<strlen($plain);$i++){
   $key.=$plain[$i]^$crypt[$i];
  }
 return $key;
}
$default_data=array("showpassword"=>"no", "bgcolor"=>"#ffffff");
$encoded="ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D";
$j=json_encode($default_data);
$x=base64_decode($encoded);
print("\nKey=".get_key($j,$x));
?>
