s=input()
arr=[]
for i in s:
    if i!='+':
        arr.append(i)
arr2=sorted(arr)
print('+'.join(arr2))

