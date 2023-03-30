a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
p=(a+b+c)/2
import math
if (a+b)>c and (a+c)>b and (b+c)>a:
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich=",round(S,3),sep="")
else:
    print("Khong hop le")