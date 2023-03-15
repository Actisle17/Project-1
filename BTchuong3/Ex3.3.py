a=float(input("x="))
b=float(input("y="))
ch=str(input("Phep toan:"))
if ch=="+":
    print(a,ch,b,"=",round(a+b,1),sep="")
elif ch=="-":
    print(a,ch,b,"=",round(a-b,1),sep="")
elif ch=="*":
    print(a,ch,b,"=",round(a*b,1),sep="")
elif ch=="/" and b!=0:
    print(a,ch,b,"=",round(a/b,1),sep="")
else:
    print("Khong hop le")