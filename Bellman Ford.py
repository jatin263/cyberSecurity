n=int(input("Enter the number of the Nodes \n --- \t"))
aas=65
nord=[]
for i in range(n):
    aass=65
    l=[]
    for j in range(n):
        if aas==aass:
            l.append(0)
        else:
            try:
                l.append(int(input(chr(aas)+" -> "+chr(aass)+" - ")))
            except:
                l.append("inf")
        aass=aass+1
    nord.append(l)
    aas=aas+1
   
print("\n\t\t -- Adjacance Matrix --\n\n") 
for j in nord:
    for k in j:
        print(k,end="\t")
    print()

print("\n\t\t -- Steps To finding Data -- \n\n")


