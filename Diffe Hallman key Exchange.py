import random

def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
	
ra=10000
prime=[]
for i in range(2,ra+1):
    if isPrime(i):
        prime.append(i)

plen=len(prime)
p=prime[random.randint(0,plen-1)]
g=prime[random.randint(0,plen-1)]
print("Public Key ( "+str(p)+" , "+str(g)+" )")
a=int(input("Enter the Private Key for Alice\n-----\t"))
b=int(input("Enter the Private Key for Bob\n-----\t"))
x=(g**a)%p
y=(g**b)%p
ka=(y**a)%p
kb=(x**b)%p
if(ka==kb):
    print("Shared Secrt Key = ",kb)
else:
    print("Not Satisfied")
