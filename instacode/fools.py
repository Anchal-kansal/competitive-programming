str=input("enter")
countf=0
countl=0
counto=0
counts=0
for char in str:
  if char=='F':
    countf+=1
  elif char=='O':
    counto+=1
  elif char=='L':
    countl+=1
  elif char=='S':
    counts+=1
  else:
    count=0
	
res=min(countf,min(int(counto/2),min(countl,counts)))	
print(res,end='')
	
