n=int(input())
print("YES" if any([n%i==0 for i in [4,7,44,47,74,77,477,447,444,777,744,774]]) else "NO")

