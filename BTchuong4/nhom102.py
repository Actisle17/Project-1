def Nhap():
    a=int(input("Nhap so muong ca phe:"))
    return a
def ketqua(a):
    canh=a//3
    cafe=a%3
    coc=canh//16
    canhconlai=canh%16
    print(str(a)+"muong ca phe chuyen doi thanh:")
    print(str(coc)+"coc,"+str(canhconlai)+"muong canh,"+str(cafe)+"muong ca phe")
a=Nhap()
ketqua(a)