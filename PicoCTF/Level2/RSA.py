#mode=sys.argv[1] #encrypt/decrypt mode
#inkey=sys.argv[2] #key
#source=sys.argv[3] #file source or stdin

import math
import random

#Euclidian Algorithm compute greatet common divisor
#output of the previous step is the input of the next
#http://www.algorithmist.com/index.php/Modular_inverse
#https://en.wikipedia.org/wiki/Euclidean_algorithm
#https://en.wikipedia.org/wiki/RSA_(cryptosystem)
def egcd(a, b): 
    if a==0:
        return b,0,1
    else:
        gcd,y,x=egcd(b%a,a)
        return gcd, x-(b//a)*y, y

#this function calculates the modular multiplicative inverse using the GCD
#computed by egcd
def modinv(a,m): 
    gcd,x,y=egcd(a,m)
    if gcd !=1:
        return None
    else:
        return x%m


#multiplication modulo n
def modmul(a,b,m):
    a=a%m
    b=b%m
    return (a*b)%m
def modadd(a,b,m):
    a=a%m
    b=b%m
    return (a+b)%m

def modpow(b,e,m):
    r=1
    while e>0:
        if e%2==1:
            r=modmul(r,b,m)
        e=e>>1
        b=modmul(b,b,m)
    return r



print('===PicoCTF 2017 Level 2 - Wierd RSA===\n\n')


c=int(95272795986475189505518980251137003509292621140166383887854853863720692420204142448424074834657149326853553097626486371206617513769930277580823116437975487148956107509247564965652417450550680181691869432067892028368985007229633943149091684419834136214793476910417359537696632874045272326665036717324623992885)
p=int(11387480584909854985125335848240384226653929942757756384489381242206157197986555243995335158328781970310603060671486688856263776452654268043936036556215243)
q=int(12972222875218086547425818961477257915105515705982283726851833508079600460542479267972050216838604649742870515200462359007315431848784163790312424462439629)
dp=int(8191957726161111880866028229950166742224147653136894248088678244548815086744810656765529876284622829884409590596114090872889522887052772791407131880103961)
dq=int(3570695757580148093370242608506191464756425954703930236924583065811730548932270595568088372441809535917032142349986828862994856575730078580414026791444659)

print('Decrypting...')
qinv=modinv(q,p)
m1=modpow(c,dp,p)
m2=modpow(c,dq,q)
if m1<m2:
    h=modmul(qinv,(m1+ceil(q/p)*p)-m2,p)
else:
    h=modmul(qinv,(m1-m2),p)
m=m2+h*q
s=str(hex(m))
print('Computed message m...',m)
print('Hex string...',s)
print('Message text...')
for i in range(2,len(s),2):
 sb=int(s[i]+s[i+1],16)
 c=chr(sb)
 print(c,end='')
print()


