def Nhap():
    x=int(input())
    k=int(input())
    n=int(input())
    L=[]
    for i in range(1,n+1):
        Y=int(input(""))
        L=L+[Y]
    return L,x,k
def add(L,x,k):
    if k>(len(L)):
        L=L+[x]
    else:
        L=L[:k-1]+[x]+L[k-1:]
        L=L[:k]+[x]+L[:k]
        L[k]=x
        return L
    def InKQ(L):
        print(L)
    L,x,k=Nhap()
    L=add(L,x,k)
    InKQ(L)