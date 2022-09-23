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
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

m=int(input("Enter the number\n"))
ra=10000
prime=[2,3]
for i in range(4,ra+1):
    if isPrime(i):
        prime[0]=prime[1]
        prime[1]=i
    if prime[0]*prime[1]>m:
        p=prime[0]
        q=prime[1]
        break
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
c=(m**e)%n
print("cyher text ",c)
mm=(c**d)%n
print("original text ",mm)


