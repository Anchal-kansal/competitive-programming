t=int(input())
arr=list(map(int,input().split(' ')))
count=0
for i in range(n):
    for j in range(i+1,n):
        if (arr[i]+arr[j])%3==0:
	        count=count+1
print(count)	  
	  
	  