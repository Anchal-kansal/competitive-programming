def factors(n):
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0:
            factorlist = factorlist + [i]
    return(factorlist)

def isprime(n):
    if (factors(n)==[1,n]):
        return(True)

def sumprimes(l):
    sum=0
    for i in range(0,len(l)):
        if isprime(l[i]):
            sum=sum+l[i]
    return(sum)



