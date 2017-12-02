n=int(input())
arr=list(map(int,input().split(' ')))
max=0
for i in range(n):
    for j in range(i+1,n):
	    if abs(arr[i]-arr[j])>max:
		    max=abs(arr[i]-arr[j])
print(max)			