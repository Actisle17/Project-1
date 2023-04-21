import math
n=int(input())
def check(n):
    i=2
    if (i<=math.sqrt(n)):
        if n%i==0:
            return False
        i=i+1
    return True
while n>=2:
    if check(n):
        print(n)
        break
    n=n-1
        