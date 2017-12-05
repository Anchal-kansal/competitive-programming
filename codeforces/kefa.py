n=int(input())
a=list(map(int,input().split()))
count=1
m=1
for i in range(0,n-1):
    if a[i]<=a[i+1]:
        count+=1
    else:
        count=1
    if m<count:
        m=count
print(m)
