def Nhap():
    n=int(input("n="))
    return n
def inkq(n):
    while True:
        for i in range (2,n+1,2):
            print(i,end=" ")
        print("")
        print("Tiep tuc khong?",end="")
        j=input()
        if j=="k" or j=="K":
            break
        else:
            n=int(input("n="))
n=Nhap()
inkq(n)        
                