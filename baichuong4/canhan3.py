def Nhap():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("b="))
    return a,b,c
def giaipt(a,b,c):
    import math
    s=b**2-4*a*c
    if s>0:
        print("Phuong trinh co hai nghiem")
        x1=(-b+math.sqrt(s))/2*a
        x2=(-b-math.sqrt(s))/2*a
        print("x1=",x1,sep="")
        print("x2=",x2,sep="")
    elif s==0:
        print("Phuong trinh co nghiem kep")
        x=-b/2*a
        print("x1=x2=",x,sep="")
    else:
        print("Phuong trinh vo nghiem")
def inkq(x1,x2):
    print("x1=",x2)
    print("x2=",x2)
a,b,c=Nhap()
giaipt(a,b,c)