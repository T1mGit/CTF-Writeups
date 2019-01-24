<h2>Forensics Warmup 1</h2>
<i>Can you unzip this file for me?</i>
<br>
<br>Unzip the file with a zip extractor such as Xarchiver to obtain the JPEG image of the flag.
<br><b>picoCTF{welcome_to_forensics}</b>
<h2>Forenics Warmup 2</h2>
<i>Hmm For some reason I cant open this png.</i>
<br>
<br>By using the Linux 'file' command or a hex editor to examine the file header you discover the file is a JPEG file not a PNG. Change the extension.
<br><b>picoCTF{extensions_are_a_lie}</b>
<h2>General Warmup 1</h2>
<i>If i told you your grade was 0x41 in hex, what is the ascii?</i>
<br>
<br>asciitable.com is a handy website.
<br><b>picoCTF{A}</b>
<h2>General Warmup 2</h2>
<i>Convert 27 (base10) to binary</i>
<br>
<br>2^4+2^3+2^1+2^0
<br><b>picoCTF{11011}</b>
<h2>General Warmup 3</h2>
<i>Convert 0x3D to decimal</i>
<br>
<br>3x16+13
<br><b>picoCTF{61}</b>
<h2>Resources</h2>
<i>We've put resources on our website https://picoctf.com/resources</i>
<br>
<br>The flag is printed on the website in plain text
<br><b>picoCTF{xiexie_ni_lai_zheli}</b>
<h2>Reversing Warmup 2</h2>
<i>Decode the string <b>dGg0dF93NHNfczFtcEwz</b></i>
<br>
<br>Cyberchef (https://gchq.github.io/CyberChef/) has lots of tools for encryption, encoding and data maniptulation. On linux use the 'base64' command.
<br><b>picoCTF{th4t_w4s_s1mpL3}</b>
<h2>Crypto Warmup 1</h2>
<i>Here is a message you got from a friend, <b>llkjmlmpadkkc</b> with the key of <b>thisisalilkey</b>. Can you use this <a href="table-1.txt">table</a> to solve it?</i>
<br>
<br>This is a Vigenere Cipher. Throw it in cyberchef.
<br><b>picoCTF{secretmessage}</b>
<h2>Crypto Warmup 2</h2>
<i>Ever heard of something called rot13</i>
<br>
<br>Rot13 is a version of the Ceaser Cipher which rotates the input letter by specified amount (this case 13, ie rot13) to a new letter. Throw it in cyberchef 
<br><b>picoCTF{this_is_crypto!}</b>
