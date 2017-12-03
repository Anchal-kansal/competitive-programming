n=int(input())
x=0
for i in range(n):
    a=list(input())
    for j in a:
        if j=='+':
            x+=1
            break
        elif j=='-':
            x-=1
            break
print(x)
