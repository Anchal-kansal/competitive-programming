n=int(input())
s=input()
count=0
for i in range(len(s)-1):
    if s[i]=='R' and s[i+1]=='R':
        count+=1
    elif s[i]=='G' and s[i+1]=='G':
        count+=1
    elif s[i]=='B' and s[i+1]=='B':
        count+=1
print(count)
        

