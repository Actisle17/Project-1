giagoc=4
def Nhap():
    print("Nhap khoang cach:")
    a=float(input())
    return a
def tongchiphi(a):
    if a<=0.14:
        chiphi=4*a
    elif a>=0.14:
        chiphi=(0.14*4)+((a-0.14)*0.25)
    return chiphi
def InKQ(tong):
    print("Tong chi phi la:",chiphi)
a=Nhap()
chiphi=tongchiphi(a)
InKQ(chiphi)