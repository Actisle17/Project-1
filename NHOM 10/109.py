def nhap():
    n=int(input("Nhap so nguyen:"))
    return n
def tinh_uoc(n):
    L=[]
    for i in range(1,n+1):
        if n%i==0:
            L.append(i)
    return L
def inkq(L,n):
    print("Uoc cua",n,"=",L)
n=nhap()
L=tinh_uoc(n)
inkq(L,n)


    
            
    