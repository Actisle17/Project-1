import math
n=int(input("n="))
if n>=2 and n<=100:
    for i in range (2,int(math.sqrt(n)+1)):
        if n%i==0:
            print(n,"khong la SNT")
            break
    else:
        print(n,'la SNT')