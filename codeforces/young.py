n=int(input())
a=[0,0,0]
for i in range(n):
    v=list(map(int,input().split()))
    a=map(sum,zip(a,v))
if any(a):
    print("NO")
else:
    print("YES")
