n=int(input())
v=[int(x) for x in input().split()]
v.sort()
if len(v)>2:
    v[0],v[1]=v[1],v[0]
    for i in range(2,len(v)-1,2):
        v[i],v[i+1]=v[i+1],v[i]
print(v,end='')  
