def gcd(a, b):
    while (b != 0):
        a, b = b, a % b
    return(a)
count=0
t=int(input())
for i in range(t):
    n=int(input())	
	for j in range(1,n+1):
	    if gcd(n,j)==1:
		    count+=1
	print(count)	 