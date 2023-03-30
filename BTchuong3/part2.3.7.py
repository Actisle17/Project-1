S=0
n=int(input("Nhap n="))
for i in range (1,1+n):
    print("So thu",i,":",sep="",end=" ")
    x=int(input())
    if x<0:
        continue
    elif x==0:
        break
    else:
        S=S+x
print("S=",S,sep="")