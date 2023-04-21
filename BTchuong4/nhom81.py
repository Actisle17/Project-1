import math
def Nhap():
    print("Nhap hai canh goc vuong:")
    a=int(input())
    b=int(input())
    return a,b
def Canhhuyen(a,b):
    c=math.sqrt(a**2+b**2)
    return c
def InKQ(c):
    print("Do dai canh huyen la:",c)
a,b=Nhap()
c=Canhhuyen(a,b) 
InKQ(c)   