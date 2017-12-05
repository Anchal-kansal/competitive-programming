n=int(input())
a=list(map(int,input().split()))
count=0
x=a.index(max(a))
y=a[::-1].index(min(a))
count=x+y
print(count-(count>=n))
