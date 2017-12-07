n=list(map(int,input()))
m=list(map(int,input()))
for a,b in zip(n,m):
    if a!=b:
        print(1,end='')
    else:
        print(0,end='')
