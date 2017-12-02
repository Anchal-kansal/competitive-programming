num=int(input())
ints = [int(x) for x in input().split()]
#len=map(int,len)
count=0
ints.sort()
for i in range(len(ints)):
  
  for j in range(i+1,len(ints)):
    
    for k in range(j+1,len(ints)):
      if ints[i]+ints[j]>ints[k]:
        count+=1
print(count,end='')	
	
