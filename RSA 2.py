def gcdd(n,m):
    if n>m:
        maxx=m
    else:
        maxx=n
    for i in range(1,maxx+1):
        if n%i==0 and m%i==0:
            ans=i
    return ans



def isPrime(n):
    #print(n)
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1



m=input("Enter the text -- ")
cyherText=''
maxx=-1
for i in m:
    if ord(i)>maxx:
        maxx=ord(i)
    
p=2
q=3
i=4
while True:
    if isPrime(i):
        p=q
        q=i
        if p*q>maxx:
            break 
    i=i+1
n=p*q
print("n = ",n)
z=(p-1)*(q-1)
print("phi = ",z)
for i in range(2,z):
    if gcdd(i,z)==1:
        e=i
        break
for j in range(1,10):
    d=((z*j)+1)/e
    if int(d)==d:
        d=int(d)  
        break
print("public key ("+str(e)+","+str(n)+")")
print("public key ("+str(d)+","+str(n)+")")
for i in m:
  cyherText = cyherText+chr((ord(i)**e)%n)
print("cyher text ",cyherText)
original=''
for i in cyherText:
  original=original+chr((ord(i)**d)%n)
print("original text ",original)


