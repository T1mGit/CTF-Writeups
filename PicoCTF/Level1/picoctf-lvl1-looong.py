import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(40.0)
s.connect(('shell2017.picoctf.com',1603))
data = s.recv(512)
string=data.decode('ascii')
print("string=",string)
#get the string from data from the port
#finding the charcters and repeats - they are enclosed in single quotes

#first character
p1=string.find(r"'")
c1=string[p1+1]

#finding repeat amount - need to work out how many characters
p1=string.find(r"'",p1+3)+1
p2=string.find(r"'",p1+1)
c2=string[p1:p2]

#find the last character
p1=string.find(r"'",p2+1)
c3=string[p1+1]

print("c1=",c1,"c2=",c2,"c3=",c3)
#convert numbers to numbers
#if c1.isdigit==True:
   # c1=int(c1)
#if c2.isdigit==True:
c2=int(c2,10)
#if c3.isdigit==True:
#c3=int(c3,10)

#print data for viewing
print("c1=",c1,"c2=",c2,"c3=",c3)


#send data
i=0
print("c1=",c1,"encoded=",c1.encode(),"c3=",c3)
c1=c1
c2
c3
c3.encode()
for i in range(0,int(c2)):
    s.send(c1.encode())
    #("c1=",c1,"encoded=",c1.encode())
s.send(c3.encode())
data=s.recv(512)
print(data.decode())
