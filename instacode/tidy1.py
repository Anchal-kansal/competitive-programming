def main():
    t=int(input())
    for i in range(t):
        n=int(input())
        while(tidy(n)):
            n-=1
            tidy(n)
        else:
            print("Case #{}: {}".format(i+1, n))
              
def tidy(n):
    if sorted(str(n)) != list(str(n)):
        return(False)
    
if __name__ == "__main__":
    main()
