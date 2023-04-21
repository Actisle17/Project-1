def LaSoNguyenTo(x):
    snt=True
    for i in range(2,x):
        if x%i==0:
            snt=False
            break  
    return snt 
def SoHopLe(x):
    if x<=1:
        so=True
    else: so=False
    return so
def NhapVaDem():
    kq=0
    print('Nhap day so:')
    while True:
        x=int(input())
        if SoHopLe(x)==False:
            if LaSoNguyenTo(x)==True:
                kq=kq+1
        else: break
    return kq           
def InKQ(kq):
    print('Co',kq,'so nguyen to')
kq=NhapVaDem()
InKQ(kq)