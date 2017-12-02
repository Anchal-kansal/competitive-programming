l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str=input()
count=0
var=[]
for i in str:
    if i in l:
        if i not in var:
	        var.append(i)
	        count += 1
print(count)	