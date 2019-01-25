<h2>grep 1</h2>
<i>find the flag in the file</i>
<br>
<br>grep the flag<b>grep pico ./file</b>
<br><b>picoCTF{grep_and_you_will_find_d66382d8}</b>

<h2> String</h2>
<i>find the flag in the file provided without running it (the file)</i>
<br>
<br>pipe the output of the 'strings' comman into 'grep' command to quickly search for the flag. <b>strings <FILEPATH> | grep pico</b>
<br>recommend using the 'mv' to change the name of the downloaded file from "strings" to avoid confusion with the 'strings' command.
<br><b>picoCTF{sTrIngS_sAVeS_Time_2fbe2166}<b>

<h2> Grep 2</h2>
<i>find the flag at the specified location</i>
<br>
<br>The folder location given in this problem contains 10 subfolders named: 'files0' to 'files9' each containing 10 files named 'file0' to 'file9'.
<br>Each file can be looped through: <b>for i in {0..9}; do for j in {0..9}; do strings ./files$i/file$j |grep pico ;done;done </b>

<h2> Inspect Me</h2>
<i>Inspect this code</i>
<br>
<br>The link takes you to a web site. To solve this use the HTML inspector in the web browser, normally obtained by pressing F12. The Flag is split in two pieces of plain text, 1) in the HTML inspector. 2) CSS Style inspector.
<br><b>picoCTF{ur_4_real_Inspect0r_g4dget_9ddb33c}</b>

<h2>Client Side is Still Bad</h2>
<i>For got my password, but doest seem to be a reset</i>
<br>
<br>Following the link you are presented with a logon box asking for a password.
<br>Entering a wrong password causes an alert saying "incorrect password"
<br>Using the HTML inspector you discover that login button references a javascript function "verify()". Examine this function you discover the flag in plain text.
<br>The function split the supplied values into substrings and compares each to substrings for the password.
<br><b>picoCTF{client_is_bad_040594}</b>

<h2>Logon</h2>
<i>I made a website for you to logon, but dont have the admin password</i>
<br>
<br>On this website if you try to guess the password you receive an error alert. but if you leave it blank you are able to "logon" but no flag.
<br>Using the Burpsuite intercept proxy in Kali Linux you can examine the HTTP request and discover a cookie being sent to you.
<br>This cookie contains values for username and password both of which are blank. There is also value "admin=False". Making this "True" and forwarding the request realises the flag.
<br><b>picoCTF{l0g1ns_ar3nt_r34l_2a968c11}</b> 

<h2>Irish Name Repo</h2>
<i>Try to log into the website</i>
<br>
<br>This website has a sidebar which has a link to an admin logon. trying to guess the password will give a logon failure.
<br>Using burpsuit to examine the requests you notice there is a paramter 'debug=0'. change this to 1 and forward the request, you are returned the output of an sql query <b>SELECT * FROM users WHERE name='' AND password=''</b>.
<br>The object is to make the statement return a true value. A comparison of <b> '1' OR '1'</b> is always true.
<br>Change put this value into the logon form minus the start and end quote because they are already included on the server side.
<br>If correct you will be logged on and see the Flag. the completed sql statment will read <b>SELECT * FROM users WHERE name='1' OR '1' AND password='1' OR '1'</b>
<br><b>picoCTF{con4n_r3411y_1snt_1r1sh_d121ca0b}</b>

<h2>Mr Robots</h2>
<i>Do you see what i see. Glimpse of flag hidden away</i>
<br>
<br>We are given a very simple site with nothing happening. No Links, No scripts. Nothing.
<br>This hint is in the name "Mr Robots". Oftern Sites have a file "robots.txt" uses for telling web spiders which part of the site is off limits.
<br>You can view this file by tying in the address bar at the root host "/robots.txt"
<br>doing this we discover a disallowed file 143ce.html, which we can navigate to and find the flag
<br><b>picoCTF{th3_w0rld_1s_4_danger0us_pl4c3_3lli0t_143ce}</b>

