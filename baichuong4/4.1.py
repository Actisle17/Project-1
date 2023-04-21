def Nhap():
    n=int(input("n="))
    return #Đưa n ra bên ngoài, trả lại kết quả của n
def giaithua(n):
    s=1
    for i in range (1,n+1):
        s=s*i
    return s
def InKQ(n,s):
    print(n,"!","=",s,sep="")
n=Nhap()
s=giathua(n)
InKQ(n,s)