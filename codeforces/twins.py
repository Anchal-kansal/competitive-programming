n=int(input())
a=sorted(list(map(int,input().split())))
b=c=0
while(b<=sum(a)):
    b=b+a.pop()
    c+=1
print(c)
        
        
