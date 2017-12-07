n=int(input())
t=' '
c=0
for i in ' '*n:
    s=input()
    if s!=t:
        c+=1
        t=s
print(c)
    
