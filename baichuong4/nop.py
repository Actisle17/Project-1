def Nhap():
    n=int(input("n="))
    return (n)
def SNT(n):
    if n>1:
        for i in range (2,n):
            if n%i==0:
                return False
        return True
def InKQ(n):
    if SNT(n)==False:
        print(n,"khong phai la SNT")
    elif SNT(n)==True:
        print(n,"La SNT")
n=Nhap()
InKQ(n)
