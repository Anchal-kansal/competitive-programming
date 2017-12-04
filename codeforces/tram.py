n=int(input())
cap=m=0
for i in range(n):
    a,b=map(int,input().split())
    cap=cap-a+b
    m=max(cap,m)
print(m)
    
    
