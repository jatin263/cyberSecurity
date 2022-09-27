def makePath(ps,nord,i,aas,vec):
    aaa=65
    for j in range(len(nord[i])):
      if nord[i][j]!=0 and nord[i][j]!='inf':
          print(chr(aas)+" - > "+chr(aaa+j),end=" ")
          ps=ps+chr(aaa+j)
          makePath(ps,nord,j,aaa+j,vec)
          print()
      vec.append(ps)
    return 0


#n=int(input("Enter the number of the Nodes \n --- \t"))
aas=65
#nord=[]
nord=[[0, 1, 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf'],
      ['inf', 0, 1, 1, 1, 'inf', 'inf', 'inf', 'inf', 'inf'],
      ['inf', 'inf', 0, 'inf', 'inf', 1, 'inf', 'inf', 'inf', 'inf'],
      ['inf', 'inf', 'inf', 0, 'inf', 'inf', 'inf', 'inf', 1, 'inf'],
      ['inf', 'inf', 'inf', 'inf', 0, 'inf', 1, 'inf', 'inf', 'inf'],
      ['inf', 'inf', 'inf', 'inf', 'inf', 0, 'inf', 1, 'inf', 'inf'],
      ['inf', 'inf', 'inf', 'inf', 'inf', 'inf', 0, 1, 'inf', 'inf'],
      ['inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 0, 'inf', 1],
      ['inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 0, 1],
      ['inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 0]]
vec=[]
ans=[]
'''for i in range(n):
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
    aas=aas+1'''
for i in nord:
  print(i)
i=0
aas=65
ps='A'
makePath(ps,nord,i,aas,vec)
