for i in range(0,5):
    p=input().split()
    if '1' in p:
        z=abs(i-2)+abs(p.index('1')-2)
print(z)
