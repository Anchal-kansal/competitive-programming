n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
value=a[k-1]
while(value==0 and k>=0):
    if k==0:
        break
    k=k-1
    value=a[k-1]

for i in a:
    if i>=value and value!=0:
        c+=1
print(c)
