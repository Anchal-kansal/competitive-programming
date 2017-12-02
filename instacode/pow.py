from math import pow
t=int(input())
for i in range(t):
    n=int(input())
    for x in range(1,int(n**0.5)):
        for y in range(1,x):
            if pow(x,y)*pow(y,x)==n:
                print(x,y)