def Nhap():
    n=int(input("n="))
    return n #Kết thúc hàm ở đây
def NhapVaDem(n):
    print("Nhap",n,"so nguyen:")
    Dem=0
    for i in range(1,n+1):
        x=int(input())
        if x%2==0 and x!=0 :
            Dem=Dem+1
    return Dem
def InKQ(kq):
    print("So chu so chan la:",kq)
n=Nhap()
kq=NhapVaDem(n)
InKQ(kq) 
    