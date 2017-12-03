n=int(input())
cout=0
for i in range(n):
    a=list(map(int,input().split()))
    count=0
    for i in a:
        if i==1:
            count+=1
    if count>=2:
        cout+=1
print(cout)
