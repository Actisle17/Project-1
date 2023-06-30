def Nhap():
    print('Nhap mot day so:')
    L=[]
    tong=0
    dem=0
    while True:
        n=int(input(''))
        if n==0:
            break
        else:
            tong+=n
            dem+=1
            L+=[n]
    return L,tong,dem

def tb(L,tong,dem):
    tb=tong/dem
    print('GTTB la:',tb)
    for i in range(len(L)):
        if L[i]>tb:
            print('So lon hon TB la:',L[i])
        elif L[i]<tb:
            print('So nho hon TB la:',L[i])
            
L,tong,dem=Nhap()
tb(L,tong,dem)